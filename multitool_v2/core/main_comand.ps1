param(
    [String]$ruta_Origen,
    [String]$ruta_Destino,
    $extensiones = @()
)
foreach($extension in $extensiones){
    foreach($elemento in Get-ChildItem -LiteralPath $ruta_Origen -Include $extensiones){
        Move-Item $elemento.FullName -Destination $ruta_Destino;
    }
}