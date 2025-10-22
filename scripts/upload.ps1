param(
  [string]$LocalFolder,
  [string]$DestUrl,
  [string]$ApplicationId,
  [string]$TenantId,
  [string]$ClientSecret
)

# --- 1) Cargar .env (desde la RAÍZ del repo) si faltan credenciales ---
if (-not $ApplicationId -or -not $TenantId -or -not $ClientSecret -or -not $LocalFolder -or -not $DestUrl) {
  # .env está en la raíz (una carpeta arriba de scripts)
  $repoRoot   = Resolve-Path (Join-Path $PSScriptRoot "..")
  $envPath    = Join-Path $repoRoot ".env"

  if (Test-Path -LiteralPath $envPath) {
    Get-Content $envPath | ForEach-Object {
      if ($_ -match '^\s*#') { return }
      if ($_ -match '^\s*$') { return }
      if ($_ -match '^(.*?)=(.*)$') {
        $name  = $matches[1].Trim()
        $value = $matches[2].Trim().Trim('"')
        [System.Environment]::SetEnvironmentVariable($name, $value)
      }
    }
  }

  if (-not $ApplicationId) { $ApplicationId = $env:AZCOPY_APPLICATION_ID }
  if (-not $TenantId)      { $TenantId      = $env:AZCOPY_TENANT_ID }
  if (-not $ClientSecret)  { $ClientSecret  = $env:AZCOPY_SPA_CLIENT_SECRET }
  if (-not $DestUrl)       { $DestUrl       = $env:AZCOPY_DEST_URL }
  if (-not $LocalFolder)   { $LocalFolder   = Join-Path $repoRoot "output" }
}

# Normaliza LocalFolder a ruta absoluta
try {
  $LocalFolder = (Resolve-Path $LocalFolder).Path
} catch {
  # dejar tal cual si no existe aún
}

# --- 2) Validaciones mínimas ---
if (-not (Get-Command azcopy -ErrorAction SilentlyContinue)) { throw "No se encontró 'azcopy' en PATH." }
if (-not (Test-Path -LiteralPath $LocalFolder)) { throw "No existe la carpeta '$LocalFolder'." }
if (-not $ApplicationId -or -not $TenantId -or -not $ClientSecret) {
  throw "Faltan credenciales: ApplicationId/TenantId/ClientSecret (pásalos como parámetros o define .env)"
}
if (-not $DestUrl) { throw "Falta DestUrl (pásalo como parámetro o define AZCOPY_DEST_URL en .env)" }

# --- 3) Login SPN ---
$env:AZCOPY_SPA_CLIENT_SECRET = $ClientSecret
Write-Host "Login SPN en AzCopy…"
azcopy login --service-principal --application-id "$ApplicationId" --tenant-id "$TenantId"
if ($LASTEXITCODE -ne 0) { throw "Login de AzCopy falló ($LASTEXITCODE)" }

# --- 4) Copia (solo ficheros nuevos o modificados) ---
Write-Host "Subiendo '$LocalFolder' a '$DestUrl'…"
azcopy copy "$LocalFolder/*" "$DestUrl" --overwrite=ifSourceNewer --from-to=LocalBlob --recursive
if ($LASTEXITCODE -ne 0) { throw "AzCopy falló ($LASTEXITCODE)" }

Write-Host "Envío completado."

# --- 5) Logout ---
Write-Host "Cerrando sesión de AzCopy…"
azcopy logout
if ($LASTEXITCODE -ne 0) {
  Write-Warning "AzCopy logout devolvió código $LASTEXITCODE (puede ignorarse si ya expiró la sesión)."
} else {
  Write-Host "Sesión cerrada correctamente."
}
