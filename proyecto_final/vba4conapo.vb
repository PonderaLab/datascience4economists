'
' data4eco
' itam
' @jcpueblita
'
'
' Algunos insights del formato de los datos:
' - Las columnas que nos interesan son: i) municipio (A-B); ii) las de los años (E-Y)
' - Los datos de las delegaciones empiezan en la fila 22
' - Hay (por alguna extraña razón) una fila vacía medio arbitraria
'

Sub quitar_filas_molestas()
' Primero, quitemos esas molestas filas vacías.
' Este truco requiere que seleccionemos desde la celda E3 hasta abajo, y después ejecutemos la macro.
'


    ' Declaraciones
    Dim c As Range  ' Declaramos la celda con tipo de dato Range
    
    
    For Each c In Selection
    
        If c = "" Then
            Range(c.Row & ":" & c.Row).Delete Shift:=xlUp
        End If
    
    Next c

End Sub

Sub rellenar_espacios_vacios_de_delegaciones()
' Rellenemos esos espacios vacios.
' Este truco requiere que seleccionemos desde la A19 hasta donde queramos rellenar.
' (También para las otras columnas [B-C] sirve)

    ' Declaraciones
    Dim c As Range      ' Declaramos la celda con tipo de dato Range
    Dim s1 As String    ' Esta variable nos va a ayudar a saber dónde vamos
    
    s1 = Range("A19").Text
    
    For Each c In Selection
    
        If c = "" Then
            c = s1
        End If
        If c.Offset(1) <> "" Then
            s1 = c.Offset(1).Text
        End If

    Next c
End Sub