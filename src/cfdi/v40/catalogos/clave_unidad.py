from enum import StrEnum


class ClaveUnidad(StrEnum):
    CU_18 = '18'
    """Tambor de cincuenta y cinco galones (EUA)"""
    CU_19 = '19'
    """Camión cisterna"""
    CU_26 = '26'
    """Tonelada real"""
    CU_29 = '29'
    """Libra por mil pies cuadrados"""
    CU_30 = '30'
    """Día de potencia de caballos por tonelada métrica de aire seco"""
    CU_31 = '31'
    """Pescar"""
    CU_32 = '32'
    """Kilogramo por tonelada métrica seca del aire"""
    CU_36 = '36'
    """Pie cúbico por minuto por pie cuadrado"""
    CU_44 = '44'
    """Bolsa a granel de quinientos kilos"""
    CU_45 = '45'
    """Bolsa a granel de trescientos kilos"""
    CU_46 = '46'
    """Bolsa a granel de cincuenta libras"""
    CU_47 = '47'
    """Bolso de cincuenta libras"""
    CU_48 = '48'
    """Carga masiva"""
    CU_53 = '53'
    """Kilogramo teórico"""
    CU_54 = '54'
    """Tonelada teórica (UK)"""
    CU_62 = '62'
    """Por ciento por 1000 horas"""
    CU_63 = '63'
    """Tasa de fracaso en el tiempo"""
    CU_64 = '64'
    """Libra por pulgada cuadrada, calibre"""
    CU_66 = '66'
    """Oersted"""
    CU_69 = '69'
    """Escala específica de prueba"""
    CU_71 = '71'
    """Voltios amperios por libra"""
    CU_72 = '72'
    """Vatio por libra"""
    CU_73 = '73'
    """Amperios por centímetro"""
    CU_76 = '76'
    """Gauss"""
    CU_78 = '78'
    """Kilogauss"""
    CU_84 = '84'
    """Kilopound-force por pulgada cuadrada"""
    CU_90 = '90'
    """Saybold segundo universal"""
    CU_92 = '92'
    """Calorías por centímetro cúbico"""
    CU_93 = '93'
    """Calorías por gramo"""
    CU_94 = '94'
    """Unidad de curl"""
    CU_95 = '95'
    """Veinte mil galones"""
    CU_96 = '96'
    """Diez mil galones (US)"""
    CU_97 = '97'
    """Diez kilos de tambor"""
    CU_98 = '98'
    """Quince kilos de tambor"""
    CU_05 = '05'
    """Ascensor"""
    CU_06 = '06'
    """Pequeño aerosol"""
    CU_08 = '08'
    """Montón de calor"""
    CU_10 = '10'
    """Grupos"""
    CU_11 = '11'
    """Equipos"""
    CU_13 = '13'
    """Raciones"""
    CU_14 = '14'
    """Shot"""
    CU_15 = '15'
    """Palo, medida militar."""
    CU_16 = '16'
    """Tambor de 115 kilogramos"""
    CU_17 = '17'
    """Tambor de cien libras"""
    CU_1A = '1A'
    """Milla de carros"""
    CU_1B = '1B'
    """Recuento de automóviles"""
    CU_1C = '1C'
    """Conteo de locomotoras"""
    CU_1D = '1D'
    """Caboose count"""
    CU_1E = '1E'
    """Coche vacío"""
    CU_1F = '1F'
    """Milla de tren"""
    CU_1G = '1G'
    """Galón del uso del combustible (los EUA)"""
    CU_1H = '1H'
    """Milla de caboose"""
    CU_1I = '1I'
    """Tipo de interés fijo"""
    CU_1J = '1J'
    """Tonelada milla"""
    CU_1K = '1K'
    """Milla locomotora"""
    CU_1L = '1L'
    """Recuento total de automóviles"""
    CU_1M = '1M'
    """Milla total del coche"""
    CU_1X = '1X'
    """Cuarto de milla"""
    CU_20 = '20'
    """Contenedores de veinte pies"""
    CU_21 = '21'
    """Contenedor de cuarenta pies"""
    CU_22 = '22'
    """Decilitro por gramo"""
    CU_23 = '23'
    """Gramo por centímetro cúbico"""
    CU_24 = '24'
    """Libra teórica"""
    CU_25 = '25'
    """Gramo por centímetro cuadrado"""
    CU_27 = '27'
    """Tonelada teórica"""
    CU_28 = '28'
    """Kilogramo por metro cuadrado"""
    CU_2A = '2A'
    """Radián por segundo"""
    CU_2B = '2B'
    """Radián por segundo cuadrado"""
    CU_2C = '2C'
    """Roentgen"""
    CU_2G = '2G'
    """Voltios CA"""
    CU_2H = '2H'
    """Voltios CD"""
    CU_2I = '2I'
    """Unidad térmica británica (tabla internacional) por hora"""
    CU_2J = '2J'
    """Centímetro cúbico por segundo"""
    CU_2K = '2K'
    """Pie cúbico por hora"""
    CU_2L = '2L'
    """Pie cúbico por minuto"""
    CU_2M = '2M'
    """Centímetro por segundo"""
    CU_2N = '2N'
    """Decibel"""
    CU_2P = '2P'
    """Kilobyte"""
    CU_2Q = '2Q'
    """Kilobecquerel"""
    CU_2R = '2R'
    """Kilocurie"""
    CU_2U = '2U'
    """Megagramo"""
    CU_2V = '2V'
    """Megagrama por hora"""
    CU_2X = '2X'
    """Metro por minuto"""
    CU_2Y = '2Y'
    """Milliroentgen"""
    CU_2Z = '2Z'
    """Milivoltio"""
    CU_33 = '33'
    """Kilopascal por grtr"""
    CU_34 = '34'
    """Kilopascal por milímetro"""
    CU_35 = '35'
    """Milímetro por un segundo centímetro cuadrado"""
    CU_37 = '37'
    """Onza por pie cuadrado"""
    CU_38 = '38'
    """Onzas por pie cuadrado por 0,01 pulgadas"""
    CU_3B = '3B'
    """Megajoule"""
    CU_3C = '3C'
    """Manmonth"""
    CU_3E = '3E'
    """Libra por libra de producto"""
    CU_3G = '3G'
    """Libra por pieza de producto"""
    CU_3H = '3H'
    """Kilogramo por kilogramo de producto"""
    CU_3I = '3I'
    """Kilogramo por pedazo de producto"""
    CU_40 = '40'
    """Mililitro por segundo"""
    CU_41 = '41'
    """Mililitro por minuto"""
    CU_4B = '4B'
    """Gorra"""
    CU_4C = '4C'
    """Centistokes"""
    CU_4E = '4E'
    """Veinte pack"""
    CU_4G = '4G'
    """Microlitro"""
    CU_4H = '4H'
    """Micra"""
    CU_4K = '4K'
    """Miliamperio"""
    CU_4L = '4L'
    """Megabyte"""
    CU_4M = '4M'
    """Miligramo por hora"""
    CU_4N = '4N'
    """Megabequerel"""
    CU_4O = '4O'
    """Microfaradio"""
    CU_4P = '4P'
    """Newton por metro"""
    CU_4Q = '4Q'
    """Onza pulgada"""
    CU_4R = '4R'
    """Onza pie"""
    CU_4T = '4T'
    """Picofaradio"""
    CU_4U = '4U'
    """Libra por hora"""
    CU_4W = '4W'
    """Tonelada (EUA) por hora"""
    CU_4X = '4X'
    """Kilolitro por hora"""
    CU_56 = '56'
    """Sitas"""
    CU_57 = '57'
    """Malla"""
    CU_58 = '58'
    """kilogramo neto"""
    CU_59 = '59'
    """Parte por millón"""
    CU_5A = '5A'
    """Barril por minuto"""
    CU_5B = '5B'
    """Batch"""
    CU_5C = '5C'
    """Galón (US) por mil"""
    CU_5E = '5E'
    """Mmscf/day"""
    CU_5F = '5F'
    """Libra por mil"""
    CU_5G = '5G'
    """bomba"""
    CU_5H = '5H'
    """Escenario"""
    CU_5I = '5I'
    """Pies cúbicos estándar"""
    CU_5J = '5J'
    """Caballos de potencia hidráulica"""
    CU_5K = '5K'
    """Contar por minuto"""
    CU_5P = '5P'
    """Nivel sísmico"""
    CU_5Q = '5Q'
    """Línea sísmica"""
    CU_60 = '60'
    """Tanto por ciento en peso"""
    CU_61 = '61'
    """Parte por mil millones (EUA)"""
    CU_74 = '74'
    """Milipascal"""
    CU_77 = '77'
    """Mili-pulgada"""
    CU_80 = '80'
    """Libra por pulgada cuadrado absoluta"""
    CU_81 = '81'
    """Henry"""
    CU_85 = '85'
    """Pie libra-fuerza"""
    CU_87 = '87'
    """Libra por pie cúbico"""
    CU_89 = '89'
    """Poise"""
    CU_91 = '91'
    """Stokes"""
    CU_A1 = 'A1'
    """15 ° C calorías"""
    CU_A10 = 'A10'
    """Amperio por metro cuadrado por joule segundo"""
    CU_A11 = 'A11'
    """Ángstrom"""
    CU_A12 = 'A12'
    """Unidad astronómica"""
    CU_A13 = 'A13'
    """Attojoule"""
    CU_A14 = 'A14'
    """Barn"""
    CU_A15 = 'A15'
    """Barn por electrovoltio"""
    CU_A16 = 'A16'
    """Barn por electrovoltio"""
    CU_A17 = 'A17'
    """Barn por esteroradian"""
    CU_A18 = 'A18'
    """Becquerel por kilogramo"""
    CU_A19 = 'A19'
    """Becquerel por metro cúbico"""
    CU_A2 = 'A2'
    """Amperio por centímetro"""
    CU_A20 = 'A20'
    """Unidad térmica británica (tabla internacional) por segundo pie cuadrado grado rankine."""
    CU_A21 = 'A21'
    """Unidad térmica británica (tabla internacional) por libra grado rankine"""
    CU_A22 = 'A22'
    """Unidad térmica británica (tabla internacional) por segundo pie grado rankine"""
    CU_A23 = 'A23'
    """Unidad térmica británica (tabla internacional) por hora pie cuadrado grado rankine."""
    CU_A24 = 'A24'
    """Candela por metro cuadrado"""
    CU_A25 = 'A25'
    """Caballo de vapor"""
    CU_A26 = 'A26'
    """Culombio metro"""
    CU_A27 = 'A27'
    """Culombio metro cuadrado por voltio"""
    CU_A28 = 'A28'
    """Culombio por centímetro cúbico"""
    CU_A29 = 'A29'
    """Culombio por metro cúbico"""
    CU_A3 = 'A3'
    """Amperio por milímetro"""
    CU_A30 = 'A30'
    """Culombio por milímetro cúbico"""
    CU_A31 = 'A31'
    """Culombio por kilogramo-segundo"""
    CU_A32 = 'A32'
    """Culombio por Mol"""
    CU_A33 = 'A33'
    """Culombio por centímetro cuadrado"""
    CU_A34 = 'A34'
    """Culombio por metro cuadrado"""
    CU_A35 = 'A35'
    """Culombio por milímetro cuadrado"""
    CU_A36 = 'A36'
    """Centímetro cúbico por Mol"""
    CU_A37 = 'A37'
    """Decímetro cuadrado por Mol"""
    CU_A38 = 'A38'
    """Cubic pooulo p"""
    CU_A39 = 'A39'
    """Metro cúbico por kilogramo"""
    CU_A4 = 'A4'
    """Amperio por centímetro cuadrado"""
    CU_A40 = 'A40'
    """Metro cúbico por Mol"""
    CU_A41 = 'A41'
    """Amperio por metro cuadrado"""
    CU_A42 = 'A42'
    """Curie por kilogramo"""
    CU_A43 = 'A43'
    """Tonelaje de peso muerto"""
    CU_A44 = 'A44'
    """Decalitro"""
    CU_A45 = 'A45'
    """Decámetro"""
    CU_A47 = 'A47'
    """Decitex"""
    CU_A48 = 'A48'
    """Grado rankine"""
    CU_A49 = 'A49'
    """Negador"""
    CU_A5 = 'A5'
    """Amperio metro cuadrado"""
    CU_A50 = 'A50'
    """Dina segundo por centímetro cúbico"""
    CU_A51 = 'A51'
    """Dina segundo por centímetro"""
    CU_A52 = 'A52'
    """Dina segundo por centímetro a la quinta potencia"""
    CU_A53 = 'A53'
    """Electronvoltio"""
    CU_A54 = 'A54'
    """Electronvoltio por metro"""
    CU_A55 = 'A55'
    """Electronvoltio por metro cuadrado"""
    CU_A56 = 'A56'
    """Electronvoltio metro cuadrado por kilogramo"""
    CU_A57 = 'A57'
    """Ergio"""
    CU_A58 = 'A58'
    """Erg por centímetro"""
    CU_A59 = 'A59'
    """La cobertura de nubes 8-parte"""
    CU_A6 = 'A6'
    """Amperio por metro cuadrado Kelvin cuadrado"""
    CU_A60 = 'A60'
    """Erg por centímetro cúbico"""
    CU_A61 = 'A61'
    """Erg por gramo"""
    CU_A62 = 'A62'
    """Erg por segundo gramo"""
    CU_A63 = 'A63'
    """Erg por segundo"""
    CU_A64 = 'A64'
    """Erg por segundo centímetro cuadrado"""
    CU_A65 = 'A65'
    """Erg por centímetro cuadrado segundo"""
    CU_A66 = 'A66'
    """Erg centímetro cuadrado"""
    CU_A67 = 'A67'
    """Erg centímetro cuadrado por gramo"""
    CU_A68 = 'A68'
    """Exajoule"""
    CU_A69 = 'A69'
    """Faradio por metro"""
    CU_A7 = 'A7'
    """Amperio por milímetro cuadrado"""
    CU_A70 = 'A70'
    """Femtojoule"""
    CU_A71 = 'A71'
    """Femtómetro"""
    CU_A73 = 'A73'
    """Pie por segundo al cuadrado"""
    CU_A74 = 'A74'
    """Pie libra-fuerza por segundo"""
    CU_A75 = 'A75'
    """Tonelada de carga"""
    CU_A76 = 'A76'
    """Galón"""
    CU_A77 = 'A77'
    """Gaussian CGS (Centímetro-Gram-Segundo sistema) unidad de desplazamiento"""
    CU_A78 = 'A78'
    """Gaussiano CGS (Centímetro-Gram-Segundo sistema) unidad de corriente eléctrica"""
    CU_A79 = 'A79'
    """Gaussian CGS (Centímetro-Gram-Segundo sistema) unidad de carga eléctrica"""
    CU_A8 = 'A8'
    """Amperio segundo"""
    CU_A80 = 'A80'
    """Gaussiano CGS (Centímetro-Gram-Segundo sistema) unidad de la fuerza del campo eléctrico"""
    CU_A81 = 'A81'
    """Gaussian CGS (Centímetro-Gram-Segundo sistema) unidad de polarización eléctrica"""
    CU_A82 = 'A82'
    """Gaussiano CGS (Centímetro-Gram-Segundo sistema) unidad de potencial eléctrico"""
    CU_A83 = 'A83'
    """Gaussian CGS (Centímetro-Gram-Segundo sistema) unidad de magnetización"""
    CU_A84 = 'A84'
    """GigaCulombio por metro cúbico"""
    CU_A85 = 'A85'
    """Gigaelectrónvoltio"""
    CU_A86 = 'A86'
    """Gigahertz"""
    CU_A87 = 'A87'
    """GigaOhm"""
    CU_A88 = 'A88'
    """GigaOhm metro"""
    CU_A89 = 'A89'
    """Gigapascal"""
    CU_A9 = 'A9'
    """Tarifa"""
    CU_A90 = 'A90'
    """Gigawatt"""
    CU_A91 = 'A91'
    """Grado centesimal"""
    CU_A93 = 'A93'
    """Gramo por metro cúbico"""
    CU_A94 = 'A94'
    """Gramo por Mol"""
    CU_A95 = 'A95'
    """Gray"""
    CU_A96 = 'A96'
    """Gray por segundo"""
    CU_A97 = 'A97'
    """Hectopascal"""
    CU_A98 = 'A98'
    """Henry por metro"""
    CU_A99 = 'A99'
    """Bit"""
    CU_AA = 'AA'
    """Balón"""
    CU_AB = 'AB'
    """Paquete a granel"""
    CU_ACR = 'ACR'
    """Acre"""
    CU_ACT = 'ACT'
    """Actividad"""
    CU_AD = 'AD'
    """Byte"""
    CU_AE = 'AE'
    """Amperio por metro"""
    CU_AH = 'AH'
    """Minuto adicional"""
    CU_AI = 'AI'
    """Minuto y medio por llamada"""
    CU_AJ = 'AJ'
    """policía"""
    CU_AK = 'AK'
    """Braza"""
    CU_AL = 'AL'
    """Línea de acceso"""
    CU_AMH = 'AMH'
    """Amperio hora"""
    CU_AMP = 'AMP'
    """Amperio"""
    CU_ANN = 'ANN'
    """Año"""
    CU_AP = 'AP'
    """Libra de aluminio solamente"""
    CU_APZ = 'APZ'
    """Onza troy u onza farmacéutica"""
    CU_AQ = 'AQ'
    """Unidad del factor anti-hemofílico."""
    CU_AR = 'AR'
    """supositorio"""
    CU_ARE = 'ARE'
    """Are"""
    CU_AS = 'AS'
    """Variedad"""
    CU_ASM = 'ASM'
    """Grado alcohólico en masa"""
    CU_ASU = 'ASU'
    """Grado alcohólico volumétrico"""
    CU_ATM = 'ATM'
    """Atmósfera estándar"""
    CU_ATT = 'ATT'
    """Atmósfera técnica"""
    CU_AW = 'AW'
    """Relleno de polvo en viales"""
    CU_AWG = 'AWG'
    """Calibre de alambre americano"""
    CU_AY = 'AY'
    """Montaje"""
    CU_AZ = 'AZ'
    """Unidad térmica británica (tabla internacional) por libra"""
    CU_B0 = 'B0'
    """Btu por pie cúbico"""
    CU_B1 = 'B1'
    """Barril (EUA) por día"""
    CU_B10 = 'B10'
    """Bits por segundo"""
    CU_B11 = 'B11'
    """Joule por kilogramo kelvin"""
    CU_B12 = 'B12'
    """Joule por metro"""
    CU_B13 = 'B13'
    """Joule por metro cuadrado"""
    CU_B14 = 'B14'
    """Joule por metro a la cuarta potencia"""
    CU_B15 = 'B15'
    """Juole por Mol"""
    CU_B16 = 'B16'
    """Juoule por Mol kelvin"""
    CU_B17 = 'B17'
    """Crédito"""
    CU_B18 = 'B18'
    """Segundos joule"""
    CU_B19 = 'B19'
    """Dígito"""
    CU_B2 = 'B2'
    """litera"""
    CU_B20 = 'B20'
    """Joule metro cuadrado por kilogramo"""
    CU_B21 = 'B21'
    """Kelvin por watt"""
    CU_B22 = 'B22'
    """Kiloamperio"""
    CU_B23 = 'B23'
    """Kiloamperio por metro cuadrado"""
    CU_B24 = 'B24'
    """Kiloamperio por metro"""
    CU_B25 = 'B25'
    """Kilobecquerel por metro cúbico"""
    CU_B26 = 'B26'
    """KiloCulombio"""
    CU_B27 = 'B27'
    """KiloCulombio por metro cúbico"""
    CU_B28 = 'B28'
    """KiloCulombio por metro cuadrado"""
    CU_B29 = 'B29'
    """Kiloelectrónvoltio"""
    CU_B3 = 'B3'
    """Libra de bateo"""
    CU_B30 = 'B30'
    """Gibibit"""
    CU_B31 = 'B31'
    """Kilogramo metro por segundo"""
    CU_B32 = 'B32'
    """Kilogramo metro cuadrado"""
    CU_B33 = 'B33'
    """Kilogramo metro cuadrado por segundo"""
    CU_B34 = 'B34'
    """Kilogramo por decímetro cúbico"""
    CU_B35 = 'B35'
    """Kilogramo por litro"""
    CU_B36 = 'B36'
    """Calorías (termoquímicas) por gramo"""
    CU_B37 = 'B37'
    """Kilogramo de fuerza"""
    CU_B38 = 'B38'
    """Kilogramo-metro de la fuerza"""
    CU_B39 = 'B39'
    """Kilogramo-fuerza del metro por segundo"""
    CU_B4 = 'B4'
    """Barril, unidad imperial"""
    CU_B40 = 'B40'
    """Kilogramo de fuerza por metro cuadrado"""
    CU_B41 = 'B41'
    """Kilojoule por kelvin"""
    CU_B42 = 'B42'
    """Kilojoule por kilogramo"""
    CU_B43 = 'B43'
    """Kilojoule por kilogramo kelvin"""
    CU_B44 = 'B44'
    """Kilojoule por Mol"""
    CU_B45 = 'B45'
    """KiloMol"""
    CU_B46 = 'B46'
    """KiloMol por metro cúbico"""
    CU_B47 = 'B47'
    """Kilonewton"""
    CU_B48 = 'B48'
    """Kilonewton metro"""
    CU_B49 = 'B49'
    """KiloOhm"""
    CU_B5 = 'B5'
    """palanquilla"""
    CU_B50 = 'B50'
    """KiloOhm metro"""
    CU_B51 = 'B51'
    """KiloLibra"""
    CU_B52 = 'B52'
    """Kilosegundo"""
    CU_B53 = 'B53'
    """Kilosiemens"""
    CU_B54 = 'B54'
    """Kilosiemens por metro"""
    CU_B55 = 'B55'
    """Kilovoltio por metro"""
    CU_B56 = 'B56'
    """Kiloweber por metro"""
    CU_B57 = 'B57'
    """Año luz"""
    CU_B58 = 'B58'
    """Litro por Mol"""
    CU_B59 = 'B59'
    """Lumen hora"""
    CU_B6 = 'B6'
    """Bollo"""
    CU_B60 = 'B60'
    """Lumen por metro cuadrado"""
    CU_B61 = 'B61'
    """Luminosidad por watt"""
    CU_B62 = 'B62'
    """Lumen segundo"""
    CU_B63 = 'B63'
    """Hora de luz"""
    CU_B64 = 'B64'
    """Segundo de luz"""
    CU_B65 = 'B65'
    """Maxwell"""
    CU_B66 = 'B66'
    """Megaamperio por metro cuadrado"""
    CU_B67 = 'B67'
    """Megabecquerel por kilogramo"""
    CU_B68 = 'B68'
    """Gigabit"""
    CU_B69 = 'B69'
    """MegaCulombio por metro cúbico"""
    CU_B7 = 'B7'
    """Ciclo"""
    CU_B70 = 'B70'
    """MegaCulombio por metro cuadrado"""
    CU_B71 = 'B71'
    """Megaelectrónvoltio"""
    CU_B72 = 'B72'
    """Megagramo por metro cúbico"""
    CU_B73 = 'B73'
    """Meganewton"""
    CU_B74 = 'B74'
    """Meganewton metro"""
    CU_B75 = 'B75'
    """MegaOhm"""
    CU_B76 = 'B76'
    """MegaOhm metro"""
    CU_B77 = 'B77'
    """Megasiemens por metro"""
    CU_B78 = 'B78'
    """Megavoltio"""
    CU_B79 = 'B79'
    """Megavoltio por metro"""
    CU_B8 = 'B8'
    """Joule por metro cúbico"""
    CU_B80 = 'B80'
    """Gigabit por segundo"""
    CU_B81 = 'B81'
    """Reciprocidad del metro cuadrado, reciprocidad del segundo"""
    CU_B82 = 'B82'
    """Pulgadas por pie lineal"""
    CU_B83 = 'B83'
    """Metro a la cuarta potencia"""
    CU_B84 = 'B84'
    """Microamperio"""
    CU_B85 = 'B85'
    """Microbar"""
    CU_B86 = 'B86'
    """MicroCulombio"""
    CU_B87 = 'B87'
    """MicroCulombio por metro cúbico"""
    CU_B88 = 'B88'
    """MicroCulombio por metro cuadrado"""
    CU_B89 = 'B89'
    """Microfaradio por metro"""
    CU_B9 = 'B9'
    """Batt"""
    CU_B90 = 'B90'
    """Microhenry"""
    CU_B91 = 'B91'
    """Microhenry por metro"""
    CU_B92 = 'B92'
    """Micronewton"""
    CU_B93 = 'B93'
    """Micronewton metro"""
    CU_B94 = 'B94'
    """Micro Ohm"""
    CU_B95 = 'B95'
    """MicroOhm metro"""
    CU_B96 = 'B96'
    """Micropascal"""
    CU_B97 = 'B97'
    """Microrradián"""
    CU_B98 = 'B98'
    """Microsegundo"""
    CU_B99 = 'B99'
    """Microsiemens"""
    CU_BAR = 'BAR'
    """Bar [unidad de presión]"""
    CU_BB = 'BB'
    """Caja base"""
    CU_BFT = 'BFT'
    """Tablero de pies"""
    CU_BH = 'BH'
    """Cepillo"""
    CU_BHP = 'BHP'
    """Potencia al freno"""
    CU_BIL = 'BIL'
    """Billón"""
    CU_BLD = 'BLD'
    """Barril seco (EUA)"""
    CU_BLL = 'BLL'
    """Barril (EUA)"""
    CU_BP = 'BP'
    """Tabledo de cien pies"""
    CU_BPM = 'BPM'
    """Latidos por minuto"""
    CU_BQL = 'BQL'
    """Becquerel"""
    CU_BTU = 'BTU'
    """Unidad térmica británica (tabla internacional)"""
    CU_BUA = 'BUA'
    """Bushel (EUA)"""
    CU_BUI = 'BUI'
    """Bushel (UK)"""
    CU_BW = 'BW'
    """Peso base"""
    CU_BZ = 'BZ'
    """Millones de BTUs"""
    CU_C0 = 'C0'
    """Llamada"""
    CU_C1 = 'C1'
    """Libra de producto compuesto (peso total)"""
    CU_C10 = 'C10'
    """Milifaradio"""
    CU_C11 = 'C11'
    """Miligalón"""
    CU_C12 = 'C12'
    """Miligramo por metro"""
    CU_C13 = 'C13'
    """MilliGray"""
    CU_C14 = 'C14'
    """Milihenry"""
    CU_C15 = 'C15'
    """Milijoule"""
    CU_C16 = 'C16'
    """Milímetro por segundo"""
    CU_C17 = 'C17'
    """Milímetro cuadrado por segundo"""
    CU_C18 = 'C18'
    """MiliMol"""
    CU_C19 = 'C19'
    """Mol por kilogramo"""
    CU_C2 = 'C2'
    """Carset"""
    CU_C20 = 'C20'
    """Milinewton"""
    CU_C21 = 'C21'
    """Kibibit"""
    CU_C22 = 'C22'
    """Milinewton por metro"""
    CU_C23 = 'C23'
    """MiliOhm metro"""
    CU_C24 = 'C24'
    """Milipascal segundo"""
    CU_C25 = 'C25'
    """Milirradián"""
    CU_C26 = 'C26'
    """Milisegundo"""
    CU_C27 = 'C27'
    """Milisiemens"""
    CU_C28 = 'C28'
    """MilliSievert"""
    CU_C29 = 'C29'
    """Militesla"""
    CU_C3 = 'C3'
    """Microvoltios por metro"""
    CU_C30 = 'C30'
    """Milivoltio por metro"""
    CU_C31 = 'C31'
    """Miliwatt"""
    CU_C32 = 'C32'
    """Miliwatt por metro cuadrado"""
    CU_C33 = 'C33'
    """Miliweber"""
    CU_C34 = 'C34'
    """Mol"""
    CU_C35 = 'C35'
    """Mol por decímetro cúbico"""
    CU_C36 = 'C36'
    """Mol por metro cúbico"""
    CU_C37 = 'C37'
    """Kilobits"""
    CU_C38 = 'C38'
    """Mol por litro"""
    CU_C39 = 'C39'
    """Nanoamperio"""
    CU_C4 = 'C4'
    """partido de carga"""
    CU_C40 = 'C40'
    """NanoCulombio"""
    CU_C41 = 'C41'
    """Nanofaradio"""
    CU_C42 = 'C42'
    """Nanofaradio por metro"""
    CU_C43 = 'C43'
    """Nanohenry"""
    CU_C44 = 'C44'
    """Nanohenry por metro"""
    CU_C45 = 'C45'
    """Nanómetro"""
    CU_C46 = 'C46'
    """NanoOhm metro"""
    CU_C47 = 'C47'
    """Nanosegundo"""
    CU_C48 = 'C48'
    """Nanotesla"""
    CU_C49 = 'C49'
    """Nanowatt"""
    CU_C5 = 'C5'
    """Costo"""
    CU_C50 = 'C50'
    """Neperio"""
    CU_C51 = 'C51'
    """Neperio por segundo"""
    CU_C52 = 'C52'
    """Picómetro"""
    CU_C53 = 'C53'
    """Newton metro segundo"""
    CU_C54 = 'C54'
    """Newton metro cuadrado por kilogramo cuadrado"""
    CU_C55 = 'C55'
    """Newton por metro cuadrado"""
    CU_C56 = 'C56'
    """Newton por milímetro cuadrado"""
    CU_C57 = 'C57'
    """Newton segundo"""
    CU_C58 = 'C58'
    """Segundos newton por metro"""
    CU_C59 = 'C59'
    """Octava"""
    CU_C6 = 'C6'
    """celda"""
    CU_C60 = 'C60'
    """Ohm centímetro"""
    CU_C61 = 'C61'
    """Ohm metro"""
    CU_C62 = 'C62'
    """Uno"""
    CU_C63 = 'C63'
    """Pársec"""
    CU_C64 = 'C64'
    """Pascal por kelvin"""
    CU_C65 = 'C65'
    """Pascal segundo"""
    CU_C66 = 'C66'
    """Segundos pascal por metro cúbico"""
    CU_C67 = 'C67'
    """Segundos pascal por metro"""
    CU_C68 = 'C68'
    """Petajoule"""
    CU_C69 = 'C69'
    """Phon"""
    CU_C7 = 'C7'
    """Centipoise"""
    CU_C70 = 'C70'
    """Picoamperio"""
    CU_C71 = 'C71'
    """PicoCulombio"""
    CU_C72 = 'C72'
    """Picofaradio por metro"""
    CU_C73 = 'C73'
    """Picohenry"""
    CU_C74 = 'C74'
    """Kilobits por segundo"""
    CU_C75 = 'C75'
    """Picowatt"""
    CU_C76 = 'C76'
    """Picowatt  por metro cuadrado"""
    CU_C77 = 'C77'
    """Calibre de libra"""
    CU_C78 = 'C78'
    """Libra fuerza"""
    CU_C79 = 'C79'
    """Kilovoltios horas amperios"""
    CU_C8 = 'C8'
    """MilliCulombio por kilogramo"""
    CU_C80 = 'C80'
    """Rad"""
    CU_C81 = 'C81'
    """Radián"""
    CU_C82 = 'C82'
    """Radianmetro cuadrado por Mol"""
    CU_C83 = 'C83'
    """Rradian metro cuadrado por kilogramo"""
    CU_C84 = 'C84'
    """Radían por metro"""
    CU_C85 = 'C85'
    """Reciprocidad Ámstrong"""
    CU_C86 = 'C86'
    """Reciprocidad del metro cúbico"""
    CU_C87 = 'C87'
    """Reciprocidad metro cúbico por segundo"""
    CU_C88 = 'C88'
    """Recíproco joule por metro cúbico"""
    CU_C89 = 'C89'
    """Henry recíproco"""
    CU_C9 = 'C9'
    """Grupo bobinas"""
    CU_C90 = 'C90'
    """Recíproco Henry"""
    CU_C91 = 'C91'
    """Reciprocidad de kelvin ó kelvin a la potencia menos 1"""
    CU_C92 = 'C92'
    """Reciprocidad Metro"""
    CU_C93 = 'C93'
    """Reciprocidad Metro cuadrado"""
    CU_C94 = 'C94'
    """Reciprocidad Minuto"""
    CU_C95 = 'C95'
    """Reciprocidad Mol"""
    CU_C96 = 'C96'
    """Reciprocidad Pascal o pascal a la potencia menos 1"""
    CU_C97 = 'C97'
    """Reciprocidad Segundo"""
    CU_C98 = 'C98'
    """Segundo recíproco por metro cúbico"""
    CU_C99 = 'C99'
    """Reciprocidad Segundo por metro cuadrado"""
    CU_CCT = 'CCT'
    """Capacidad de carga en toneladas métricas"""
    CU_CDL = 'CDL'
    """Candela"""
    CU_CE = 'CE'
    """Cada mes"""
    CU_CEL = 'CEL'
    """Grados celsius"""
    CU_CEN = 'CEN'
    """Centenar"""
    CU_CG = 'CG'
    """Tarjeta"""
    CU_CGM = 'CGM'
    """Centigramo"""
    CU_CK = 'CK'
    """Conector"""
    CU_CKG = 'CKG'
    """Culombio por kilogramo"""
    CU_CLF = 'CLF'
    """Cientos de hojas"""
    CU_CLT = 'CLT'
    """Centilitro"""
    CU_CMK = 'CMK'
    """Centímetro cuadrado"""
    CU_CMQ = 'CMQ'
    """Centímetro cúbico"""
    CU_CMT = 'CMT'
    """Centímetro"""
    CU_CNP = 'CNP'
    """Cientos de paquetes"""
    CU_CNT = 'CNT'
    """Cental (UK)"""
    CU_COU = 'COU'
    """Culombio"""
    CU_CTG = 'CTG'
    """Contenido en gramos"""
    CU_CTM = 'CTM'
    """Quilatage métrico"""
    CU_CTN = 'CTN'
    """Tonelada de contenido (métrica)"""
    CU_CUR = 'CUR'
    """Curie"""
    CU_CWA = 'CWA'
    """Hundred pound"""
    CU_CWI = 'CWI'
    """Hundredweight"""
    CU_CZ = 'CZ'
    """Combo"""
    CU_D03 = 'D03'
    """Kilovatio hora por hora"""
    CU_D04 = 'D04'
    """Lot [unidad de peso]"""
    CU_D1 = 'D1'
    """Segundo recíproco por estereorradián"""
    CU_D10 = 'D10'
    """Siemens por metro"""
    CU_D11 = 'D11'
    """Mebibit"""
    CU_D12 = 'D12'
    """Siemens metro cuadrado por Mol"""
    CU_D13 = 'D13'
    """Sievert"""
    CU_D14 = 'D14'
    """Yarda mil lineal"""
    CU_D15 = 'D15'
    """Sone"""
    CU_D16 = 'D16'
    """Centímetro cuadrado por erg"""
    CU_D17 = 'D17'
    """Centímetro cuadrado por esteroradian erg"""
    CU_D18 = 'D18'
    """Metro kelvin"""
    CU_D19 = 'D19'
    """Metro cuadrado kelvin por watt."""
    CU_D2 = 'D2'
    """Segundo recíproco por estereorradián metro cuadrado"""
    CU_D20 = 'D20'
    """Metro cuadrado por joule"""
    CU_D21 = 'D21'
    """Metro cuadrado por kilogramo"""
    CU_D22 = 'D22'
    """Metro cuadrado por Mol"""
    CU_D23 = 'D23'
    """Gramo pluma (proteína)"""
    CU_D24 = 'D24'
    """Metro cuadrado por esteroradian"""
    CU_D25 = 'D25'
    """Metro cuadrado por esteroradian joule"""
    CU_D26 = 'D26'
    """Metro cuadrado por voltiosegundo"""
    CU_D27 = 'D27'
    """Estereorradían"""
    CU_D28 = 'D28'
    """sifón"""
    CU_D29 = 'D29'
    """Terahertz"""
    CU_D30 = 'D30'
    """Terajoule"""
    CU_D31 = 'D31'
    """Terawatt"""
    CU_D32 = 'D32'
    """Terawatt hora"""
    CU_D33 = 'D33'
    """Tesla"""
    CU_D34 = 'D34'
    """Tex"""
    CU_D35 = 'D35'
    """Calorías (termoquímicas)"""
    CU_D36 = 'D36'
    """Megabit"""
    CU_D37 = 'D37'
    """Calorías (termoquímicas) por gramo de kelvin"""
    CU_D38 = 'D38'
    """Calorías (termoquímicas) por segundo centímetro kelvin"""
    CU_D39 = 'D39'
    """Calorías (termoquímicas) por segundo centímetro cuadrado kelvin"""
    CU_D40 = 'D40'
    """Mil litros"""
    CU_D41 = 'D41'
    """Tonelada por metro cúbico"""
    CU_D42 = 'D42'
    """Año tropical"""
    CU_D43 = 'D43'
    """Unidad de masa atómica unificada"""
    CU_D44 = 'D44'
    """Var"""
    CU_D45 = 'D45'
    """Voltio cuadrado por kelvin cuadrado"""
    CU_D46 = 'D46'
    """Voltioio-amperio"""
    CU_D47 = 'D47'
    """Voltio por centímetro"""
    CU_D48 = 'D48'
    """Voltio por Kelvin"""
    CU_D49 = 'D49'
    """Millivoltio por Kelvin"""
    CU_D5 = 'D5'
    """Kilogramo por centímetro cuadrado"""
    CU_D50 = 'D50'
    """Voltio por metro"""
    CU_D51 = 'D51'
    """Voltio por milímetro"""
    CU_D52 = 'D52'
    """Watt por kelvin"""
    CU_D53 = 'D53'
    """Watt por metro kelvin"""
    CU_D54 = 'D54'
    """Watt por metro cuadrado"""
    CU_D55 = 'D55'
    """Watt por metro cuadrado kelvin"""
    CU_D56 = 'D56'
    """Watt por metro cuadrado kelvin a la cuarta potencia"""
    CU_D57 = 'D57'
    """Watt por estereorradián"""
    CU_D58 = 'D58'
    """Watt por estereorradián metro cuadrado"""
    CU_D59 = 'D59'
    """Weber por metro"""
    CU_D6 = 'D6'
    """Roentgen por segundo"""
    CU_D60 = 'D60'
    """Weber por milímetro"""
    CU_D61 = 'D61'
    """Minuto [unidad de ángulo]"""
    CU_D62 = 'D62'
    """Segundo [unidad de ángulo]"""
    CU_D63 = 'D63'
    """Libro"""
    CU_D64 = 'D64'
    """bloquear"""
    CU_D65 = 'D65'
    """Redondo"""
    CU_D66 = 'D66'
    """casete"""
    CU_D67 = 'D67'
    """Dólar por hora"""
    CU_D68 = 'D68'
    """Número de palabras"""
    CU_D69 = 'D69'
    """Pulgada a la cuarta potencia"""
    CU_D7 = 'D7'
    """Sandwich"""
    CU_D70 = 'D70'
    """Calorías (tabla internacional)"""
    CU_D71 = 'D71'
    """Calorías (tabla internacional) por segundo centímetro kelvin"""
    CU_D72 = 'D72'
    """Calorías (tabla internacional) por segundo centímetro cuadrado kelvin"""
    CU_D73 = 'D73'
    """Joule metro cuadrado"""
    CU_D74 = 'D74'
    """Kilogramo por Mol"""
    CU_D75 = 'D75'
    """Calorías (tabla internacional) por gramo"""
    CU_D76 = 'D76'
    """Calorías (tabla internacional) por gramo de kelvin"""
    CU_D77 = 'D77'
    """MegaCulombio"""
    CU_D78 = 'D78'
    """Megajoule por segundo"""
    CU_D79 = 'D79'
    """Viga"""
    CU_D8 = 'D8'
    """Draize score"""
    CU_D80 = 'D80'
    """Microwatt"""
    CU_D81 = 'D81'
    """Microtesla"""
    CU_D82 = 'D82'
    """Microvoltio"""
    CU_D83 = 'D83'
    """Milinewton metro"""
    CU_D85 = 'D85'
    """Microwatt por metro cuadrado"""
    CU_D86 = 'D86'
    """MiliCulombio"""
    CU_D87 = 'D87'
    """MiliMol por kilogramo"""
    CU_D88 = 'D88'
    """MiliCulombio por metro cúbico"""
    CU_D89 = 'D89'
    """MiliCulombio por metro cuadrado"""
    CU_D9 = 'D9'
    """Dina por centímetro cuadrado"""
    CU_D90 = 'D90'
    """Metro cúbico (neta)"""
    CU_D91 = 'D91'
    """Rem"""
    CU_D92 = 'D92'
    """banda"""
    CU_D93 = 'D93'
    """Segundo por metro cúbico"""
    CU_D94 = 'D94'
    """Segundo por metro cúbico Radian"""
    CU_D95 = 'D95'
    """Joule por gramo"""
    CU_D96 = 'D96'
    """Libra bruta"""
    CU_D98 = 'D98'
    """Libra masiva"""
    CU_D99 = 'D99'
    """manga"""
    CU_DAA = 'DAA'
    """Decar"""
    CU_DAD = 'DAD'
    """Decena de días"""
    CU_DAY = 'DAY'
    """Día"""
    CU_DB = 'DB'
    """Libra seca"""
    CU_DC = 'DC'
    """Disco (disco)"""
    CU_DD = 'DD'
    """Grado [unidad de ángulo]"""
    CU_DE = 'DE'
    """Acuerdo"""
    CU_DEC = 'DEC'
    """Década"""
    CU_DG = 'DG'
    """Decigramo"""
    CU_DI = 'DI'
    """dispensador"""
    CU_DJ = 'DJ'
    """Decagramo"""
    CU_DLT = 'DLT'
    """Decilitro"""
    CU_DMA = 'DMA'
    """Decámetro cúbico"""
    CU_DMK = 'DMK'
    """Decímetro cuadrado"""
    CU_DMO = 'DMO'
    """Kiloliter norma"""
    CU_DMQ = 'DMQ'
    """Decímetro cúbico"""
    CU_DMT = 'DMT'
    """Decímetro"""
    CU_DN = 'DN'
    """Decinewton metro"""
    CU_DPC = 'DPC'
    """Docenas de piezas"""
    CU_DPR = 'DPR'
    """Docenas de pares"""
    CU_DPT = 'DPT'
    """Peso de desplazamiento"""
    CU_DQ = 'DQ'
    """registro de datos"""
    CU_DRA = 'DRA'
    """Dram (EUA)"""
    CU_DRI = 'DRI'
    """Dram (UK)"""
    CU_DRL = 'DRL'
    """Docena de rodillos"""
    CU_DRM = 'DRM'
    """Drachm (UK)"""
    CU_DS = 'DS'
    """monitor"""
    CU_DT = 'DT'
    """Tonelada seca"""
    CU_DTN = 'DTN'
    """Decitonelada métrica"""
    CU_DU = 'DU'
    """dina"""
    CU_DWT = 'DWT'
    """Pennyweight"""
    CU_Dx = 'Dx'
    """Dina por centímetro"""
    CU_DY = 'DY'
    """Libro de directorio"""
    CU_DZN = 'DZN'
    """Docena"""
    CU_DZP = 'DZP'
    """Docena de paquete"""
    CU_E01 = 'E01'
    """Newton por centímetro cuadrado"""
    CU_E07 = 'E07'
    """Megawatt hora por hora"""
    CU_E08 = 'E08'
    """Megavatios por hertz"""
    CU_E09 = 'E09'
    """Miliamperio hora"""
    CU_E10 = 'E10'
    """Día de grado"""
    CU_E11 = 'E11'
    """Gigacalorie"""
    CU_E12 = 'E12'
    """Mille"""
    CU_E14 = 'E14'
    """Kilocaloría (tabla internacional)"""
    CU_E15 = 'E15'
    """Kilocaloría (termoquímica) por hora"""
    CU_E16 = 'E16'
    """Millón de btu (ti) por hora"""
    CU_E17 = 'E17'
    """Pie cúbico por segundo"""
    CU_E18 = 'E18'
    """Tonelada por hora"""
    CU_E19 = 'E19'
    """Ping"""
    CU_E20 = 'E20'
    """Megabit por segundo"""
    CU_E21 = 'E21'
    """Shares"""
    CU_E22 = 'E22'
    """Tue"""
    CU_E23 = 'E23'
    """Neumático"""
    CU_E25 = 'E25'
    """Unidad activa"""
    CU_E27 = 'E27'
    """Dosis"""
    CU_E28 = 'E28'
    """Tonelada seca de aire"""
    CU_E3 = 'E3'
    """remolque"""
    CU_E30 = 'E30'
    """Hebra"""
    CU_E31 = 'E31'
    """Metro cuadrado por litro"""
    CU_E32 = 'E32'
    """Litros por hora"""
    CU_E33 = 'E33'
    """Por mil pies"""
    CU_E34 = 'E34'
    """Gigabyte"""
    CU_E35 = 'E35'
    """Terabyte"""
    CU_E36 = 'E36'
    """Petabyte"""
    CU_E37 = 'E37'
    """Pixel"""
    CU_E38 = 'E38'
    """Megapíxeles"""
    CU_E39 = 'E39'
    """Puntos por pulgada"""
    CU_E4 = 'E4'
    """Kilo bruto"""
    CU_E40 = 'E40'
    """Parte por cien mil"""
    CU_E41 = 'E41'
    """Kilogramo-fuerza por milímetro cuadrado"""
    CU_E42 = 'E42'
    """Kilogramo-fuerza por centímetro cuadrado"""
    CU_E43 = 'E43'
    """Joule por centímetro cuadrado"""
    CU_E44 = 'E44'
    """Metros kilogramo-fuerza por centímetro cuadrado"""
    CU_E45 = 'E45'
    """MiliOhm"""
    CU_E46 = 'E46'
    """Kilovatio hora por metro cúbico"""
    CU_E47 = 'E47'
    """Kilovatio hora por kelvin"""
    CU_E48 = 'E48'
    """Unidad de servicio"""
    CU_E49 = 'E49'
    """Día de trabajo"""
    CU_E5 = 'E5'
    """Tonelada métrica larga"""
    CU_E50 = 'E50'
    """Unidad de cuenta"""
    CU_E51 = 'E51'
    """Trabajo"""
    CU_E52 = 'E52'
    """Run foot"""
    CU_E53 = 'E53'
    """Prueba"""
    CU_E54 = 'E54'
    """Viaje"""
    CU_E55 = 'E55'
    """Utilizar"""
    CU_E56 = 'E56'
    """Bien"""
    CU_E57 = 'E57'
    """Zona"""
    CU_E58 = 'E58'
    """Exabit por segundo"""
    CU_E59 = 'E59'
    """Exbibyte"""
    CU_E60 = 'E60'
    """Pebibyte"""
    CU_E61 = 'E61'
    """Tebibyte"""
    CU_E62 = 'E62'
    """Gibibyte"""
    CU_E63 = 'E63'
    """Mebibyte"""
    CU_E64 = 'E64'
    """Kibibyte"""
    CU_E65 = 'E65'
    """Exbibit por metro"""
    CU_E66 = 'E66'
    """Exbibit por metro cuadrado"""
    CU_E67 = 'E67'
    """Exbibit por metro cúbico"""
    CU_E68 = 'E68'
    """Gigabyte por segundo"""
    CU_E69 = 'E69'
    """Gibibit por metro"""
    CU_E70 = 'E70'
    """Gibibit por metro cuadrado"""
    CU_E71 = 'E71'
    """Gibibit por metro cúbico"""
    CU_E72 = 'E72'
    """Kibibit por metro"""
    CU_E73 = 'E73'
    """Kibibit por metro cuadrado"""
    CU_E74 = 'E74'
    """Kikibit por metro cúbico."""
    CU_E75 = 'E75'
    """Mebbit por metro."""
    CU_E76 = 'E76'
    """Mebbitt por metro cuadrado."""
    CU_E77 = 'E77'
    """Mebbit por metro cúbico."""
    CU_E78 = 'E78'
    """Petabit"""
    CU_E79 = 'E79'
    """Pebibit por segundo."""
    CU_E80 = 'E80'
    """Pebibit por metro."""
    CU_E81 = 'E81'
    """Pebibit por metro cuadrado."""
    CU_E82 = 'E82'
    """Pebibit por metro cúbico."""
    CU_E83 = 'E83'
    """Tebibit."""
    CU_E84 = 'E84'
    """Tebibit por segundo"""
    CU_E85 = 'E85'
    """Tebibit por metro."""
    CU_E86 = 'E86'
    """Tebibit por metro cúbico."""
    CU_E87 = 'E87'
    """Tebibit por metro cuadrado"""
    CU_E88 = 'E88'
    """Bit por metro"""
    CU_E89 = 'E89'
    """Bit por metro cuadrado"""
    CU_E90 = 'E90'
    """Centímetro recíproco"""
    CU_E91 = 'E91'
    """Día recíproco"""
    CU_E92 = 'E92'
    """Decímetro cúbico por hora"""
    CU_E93 = 'E93'
    """Kilogramo por hora"""
    CU_E94 = 'E94'
    """KiloMol por segundo"""
    CU_E95 = 'E95'
    """Mol por segundo"""
    CU_E96 = 'E96'
    """Grado por segundo"""
    CU_E97 = 'E97'
    """Mililitro por gadro celsius metro"""
    CU_E98 = 'E98'
    """Grado celsius por kelvin"""
    CU_E99 = 'E99'
    """Hectopascal por bar"""
    CU_EA = 'EA'
    """Elemento"""
    CU_EB = 'EB'
    """Casilla de correo electrónico"""
    CU_EP = 'EP'
    """Paquete de once"""
    CU_EQ = 'EQ'
    """Galón equivalente"""
    CU_F01 = 'F01'
    """Bit por metro cúbico"""
    CU_F02 = 'F02'
    """Kelvin por kelvin"""
    CU_F03 = 'F03'
    """Kilopascal por bar"""
    CU_F04 = 'F04'
    """Milibar por bar"""
    CU_F05 = 'F05'
    """Megapascal por bar"""
    CU_F06 = 'F06'
    """Poise por bar"""
    CU_F07 = 'F07'
    """Pascal por bar"""
    CU_F08 = 'F08'
    """Miliamperio por pulgada"""
    CU_F1 = 'F1'
    """Mil pies cúbicos por día"""
    CU_F10 = 'F10'
    """Kelvin por hora"""
    CU_F11 = 'F11'
    """Kelvin por minuto"""
    CU_F12 = 'F12'
    """Kelvin por segundo"""
    CU_F13 = 'F13'
    """Slug"""
    CU_F14 = 'F14'
    """Gramo por kelvin"""
    CU_F15 = 'F15'
    """Kilogramo por kelvin"""
    CU_F16 = 'F16'
    """Miligramo por kelvin"""
    CU_F17 = 'F17'
    """Libra fuerza por pie"""
    CU_F18 = 'F18'
    """Kilogramo centímetro cuadrado"""
    CU_F19 = 'F19'
    """Kilogramo milimetro cuadrado"""
    CU_F20 = 'F20'
    """Libra pulgada cuadrada"""
    CU_F21 = 'F21'
    """Libra fuerza pulgada"""
    CU_F22 = 'F22'
    """Libra fuerza por pie entre amperio"""
    CU_F23 = 'F23'
    """Gramo por decímetro cúbico"""
    CU_F24 = 'F24'
    """Kilogramo por kiloMol"""
    CU_F25 = 'F25'
    """Gramo por hertz"""
    CU_F26 = 'F26'
    """Gramo por día"""
    CU_F27 = 'F27'
    """Gramo por hora"""
    CU_F28 = 'F28'
    """Gramo por minuto"""
    CU_F29 = 'F29'
    """Gramo por segundo"""
    CU_F30 = 'F30'
    """Kilogramo por día"""
    CU_F31 = 'F31'
    """Kilogramo por minuto"""
    CU_F32 = 'F32'
    """Miligramo por dia"""
    CU_F33 = 'F33'
    """Miligramo por minuto"""
    CU_F34 = 'F34'
    """Miligramo por segundo"""
    CU_F35 = 'F35'
    """Gramo por día kelvin"""
    CU_F36 = 'F36'
    """Gramo por hora kelvin"""
    CU_F37 = 'F37'
    """Gramo por minuto kelvin"""
    CU_F38 = 'F38'
    """Gramo por segundo kelvin"""
    CU_F39 = 'F39'
    """Kilogramo por día kelvin"""
    CU_F40 = 'F40'
    """Kilogramo por hora kelvin"""
    CU_F41 = 'F41'
    """Kilogramo por minuto kelvin"""
    CU_F42 = 'F42'
    """Kilogramo por segundo kelvin"""
    CU_F43 = 'F43'
    """Miligramo por día kelvin"""
    CU_F44 = 'F44'
    """Miligramo por hora kelvin"""
    CU_F45 = 'F45'
    """Miligramo por minuto kelvin"""
    CU_F46 = 'F46'
    """Miligramo por segundo kelvin"""
    CU_F47 = 'F47'
    """Newton por milímetro"""
    CU_F48 = 'F48'
    """Libra fuerza por pulgada"""
    CU_F49 = 'F49'
    """Rod (Unidad de distancia)"""
    CU_F50 = 'F50'
    """Micrómetro por kelvin"""
    CU_F51 = 'F51'
    """Centímetro por kelvin"""
    CU_F52 = 'F52'
    """Metro por kelvin"""
    CU_F53 = 'F53'
    """Mililitro por kelvin"""
    CU_F54 = 'F54'
    """MiliOhm por metro"""
    CU_F55 = 'F55'
    """Ohm por milla (milla estatal)"""
    CU_F56 = 'F56'
    """Ohm por kilómetro"""
    CU_F57 = 'F57'
    """Miliamperio por libra-fuerza por pulgada cuadrada"""
    CU_F58 = 'F58'
    """Bar recíproco"""
    CU_F59 = 'F59'
    """Miliamperio por bar"""
    CU_F60 = 'F60'
    """Grado celsius por bar"""
    CU_F61 = 'F61'
    """Kelvin por bar"""
    CU_F62 = 'F62'
    """Gramo por día bar"""
    CU_F63 = 'F63'
    """Gramo por hora bar"""
    CU_F64 = 'F64'
    """Gramo por minuto bar"""
    CU_F65 = 'F65'
    """Gramo por segundo bar"""
    CU_F66 = 'F66'
    """Kililogramo por día bar"""
    CU_F67 = 'F67'
    """Kilogramo por hora bar"""
    CU_F68 = 'F68'
    """Kilogramo por minuto bar"""
    CU_F69 = 'F69'
    """Kilogramo por segundo bar"""
    CU_F70 = 'F70'
    """Miligramo por día bar"""
    CU_F71 = 'F71'
    """Miligramo por hora bar"""
    CU_F72 = 'F72'
    """Miligramo por minuto bar"""
    CU_F73 = 'F73'
    """Miligramo por segundo bar"""
    CU_F74 = 'F74'
    """Gramo por bar"""
    CU_F75 = 'F75'
    """Miligramo por bar"""
    CU_F76 = 'F76'
    """Miliamperio por milímetro"""
    CU_F77 = 'F77'
    """Pascal segundo por kelvin"""
    CU_F78 = 'F78'
    """Pulgada de agua"""
    CU_F79 = 'F79'
    """Pulgada de mercurio"""
    CU_F80 = 'F80'
    """Caballos de fuerza de agua"""
    CU_F81 = 'F81'
    """Bar por kelvin"""
    CU_F82 = 'F82'
    """Hectopascal por kelvin"""
    CU_F83 = 'F83'
    """Kilopascal por kelvin"""
    CU_F84 = 'F84'
    """Milibar por kelvin"""
    CU_F85 = 'F85'
    """Megapascal por kelvin"""
    CU_F86 = 'F86'
    """Poise por kelvin"""
    CU_F87 = 'F87'
    """Voltio por litro minuto"""
    CU_F88 = 'F88'
    """Newton centímetro"""
    CU_F89 = 'F89'
    """Newton metro por grados"""
    CU_F9 = 'F9'
    """Fibra por centímetro cúbico de aire"""
    CU_F90 = 'F90'
    """Newton metro por amperio"""
    CU_F91 = 'F91'
    """Bar litro por segundo"""
    CU_F92 = 'F92'
    """Bar metro cúbico por segundo"""
    CU_F93 = 'F93'
    """Hectopascal litro por segundo"""
    CU_F94 = 'F94'
    """Hectopascal metro cúbico por segundo"""
    CU_F95 = 'F95'
    """Milibar litro por segundo"""
    CU_F96 = 'F96'
    """Milibar metro cúbico por segundo"""
    CU_F97 = 'F97'
    """Megapascal litro por segundo"""
    CU_F98 = 'F98'
    """Megapascal metro cúbico por segundo"""
    CU_F99 = 'F99'
    """Pascal litro por segundo"""
    CU_FAH = 'FAH'
    """Grado fahrenheit"""
    CU_FAR = 'FAR'
    """Farad"""
    CU_FB = 'FB'
    """campo"""
    CU_FBM = 'FBM'
    """Medidor de fibra"""
    CU_FC = 'FC'
    """Mil pies cúbicos"""
    CU_FD = 'FD'
    """Millones de partículas por pie cúbico"""
    CU_FE = 'FE'
    """Pie de pista"""
    CU_FF = 'FF'
    """Cien metros cúbicos"""
    CU_FG = 'FG'
    """Parche transdérmico"""
    CU_FH = 'FH'
    """MicroMol"""
    CU_FIT = 'FIT'
    """Fallas en el tiempo"""
    CU_FL = 'FL'
    """Flake ton"""
    CU_FM = 'FM'
    """Millones de pies cúbicos"""
    CU_FOT = 'FOT'
    """Pie"""
    CU_FP = 'FP'
    """Libra por pie cuadrado"""
    CU_FR = 'FR'
    """Pie por minuto"""
    CU_FS = 'FS'
    """Pie por segundo"""
    CU_FTK = 'FTK'
    """Pie cuadrado"""
    CU_FTQ = 'FTQ'
    """Pie cúbico"""
    CU_G01 = 'G01'
    """Pascal metro cúbico por segundo"""
    CU_G04 = 'G04'
    """Centímetro por bar"""
    CU_G05 = 'G05'
    """Metro por bar"""
    CU_G06 = 'G06'
    """Milímetro por bar"""
    CU_G08 = 'G08'
    """Pulgada cuadrada por segundo"""
    CU_G09 = 'G09'
    """Metro cuadrado por segundo kelvin"""
    CU_G10 = 'G10'
    """Stokes por kelvin"""
    CU_G11 = 'G11'
    """Gramo por centímetro cúbico bar"""
    CU_G12 = 'G12'
    """Gramo por decímetro cúbico bar"""
    CU_G13 = 'G13'
    """Gramo por litro bar"""
    CU_G14 = 'G14'
    """Gramo por metro cúbico bar"""
    CU_G15 = 'G15'
    """Gramo por mililitro bar"""
    CU_G16 = 'G16'
    """Kilogramo por centímetro cúbico bar"""
    CU_G17 = 'G17'
    """Kilogramo por litro bar"""
    CU_G18 = 'G18'
    """Kilogramo por metro cúbico bar"""
    CU_G19 = 'G19'
    """Newton metro por kilogramo"""
    CU_G2 = 'G2'
    """Galón (EUA) por minuto"""
    CU_G20 = 'G20'
    """Libra-fuerza pie por libra"""
    CU_G21 = 'G21'
    """Taza (unidad de volumen)"""
    CU_G23 = 'G23'
    """Peck"""
    CU_G24 = 'G24'
    """Cucharada (estados unidos)"""
    CU_G25 = 'G25'
    """Cucharilla (estados unidos)"""
    CU_G26 = 'G26'
    """Estere"""
    CU_G27 = 'G27'
    """Centímetro cúbico por kelvin"""
    CU_G28 = 'G28'
    """Litro por kelvin"""
    CU_G29 = 'G29'
    """Metro cúbico por kelvin"""
    CU_G3 = 'G3'
    """Galón (RU) por minuto"""
    CU_G30 = 'G30'
    """Mililitro por klevin"""
    CU_G31 = 'G31'
    """Kilogramo por centímetro cúbico"""
    CU_G32 = 'G32'
    """Onza (avoirdupois) por yarda cúbica"""
    CU_G33 = 'G33'
    """Gramo por centímetro cúbico kelvin"""
    CU_G34 = 'G34'
    """Gramo por decímetro cúbico kelvin"""
    CU_G35 = 'G35'
    """Gramo por litro kelvin"""
    CU_G36 = 'G36'
    """Gramo por metro cúbico kelvin"""
    CU_G37 = 'G37'
    """Gramo por mililitro kelvin"""
    CU_G38 = 'G38'
    """Kilogramo por centímetro cúbico kelvin"""
    CU_G39 = 'G39'
    """Kilogramo por litro kelvin"""
    CU_G40 = 'G40'
    """Kilogramo por metro cúbico kelvin"""
    CU_G41 = 'G41'
    """Metro cuadrado por segundo bar"""
    CU_G42 = 'G42'
    """Microsiemens por centímetro"""
    CU_G43 = 'G43'
    """Microsiemens por metro"""
    CU_G44 = 'G44'
    """Nanosiemens por centímetro"""
    CU_G45 = 'G45'
    """Nanosiemens por metro"""
    CU_G46 = 'G46'
    """Stokes por bar"""
    CU_G47 = 'G47'
    """Centímetro cúbico por día"""
    CU_G48 = 'G48'
    """Centímetro cúbico por hora"""
    CU_G49 = 'G49'
    """Centímetro cúbico por minuto"""
    CU_G50 = 'G50'
    """Galón por hora"""
    CU_G51 = 'G51'
    """Litro por segundo"""
    CU_G52 = 'G52'
    """Metro cúbico por día"""
    CU_G53 = 'G53'
    """Metro cúbico por minuto"""
    CU_G54 = 'G54'
    """Mililitro por día"""
    CU_G55 = 'G55'
    """Mililitro por hora"""
    CU_G56 = 'G56'
    """Pulgada cúbica por hora"""
    CU_G57 = 'G57'
    """Pulgada cúbica por minuto"""
    CU_G58 = 'G58'
    """Pulgada cúbica por segundo"""
    CU_G59 = 'G59'
    """Miliamperio por litro minuto"""
    CU_G60 = 'G60'
    """Voltio por bar"""
    CU_G61 = 'G61'
    """Centímetro cúbico por día kelvin"""
    CU_G62 = 'G62'
    """Centímetro cúbico por hora kelvin"""
    CU_G63 = 'G63'
    """Centímetro cúbico por minuto kelvin"""
    CU_G64 = 'G64'
    """Centímetro cúbico por segundo kelvin"""
    CU_G65 = 'G65'
    """Litro por día kelvin"""
    CU_G66 = 'G66'
    """Litro por hora kelvin"""
    CU_G67 = 'G67'
    """Litro por minuto kelvin"""
    CU_G68 = 'G68'
    """Litro por segundo kelvin"""
    CU_G69 = 'G69'
    """Metro cúbico por día kelvin"""
    CU_G7 = 'G7'
    """Hoja de microficha"""
    CU_G70 = 'G70'
    """Metro cúbico por hora kelvin"""
    CU_G71 = 'G71'
    """Metro cúbico por minuto kelvin"""
    CU_G72 = 'G72'
    """Metro cúbico por segundo kelvin"""
    CU_G73 = 'G73'
    """Mililitro por día kelvin"""
    CU_G74 = 'G74'
    """Mililitro por hora kelvin"""
    CU_G75 = 'G75'
    """Mililitro por minuto kelvin"""
    CU_G76 = 'G76'
    """Mililitro por segundo kelvin"""
    CU_G77 = 'G77'
    """Milímetro a la cuarta potencia"""
    CU_G78 = 'G78'
    """Centímetro cúbico por día bar"""
    CU_G79 = 'G79'
    """Centímetro cúbico por hora bar"""
    CU_G80 = 'G80'
    """Centímetro cúbico por minuto bar"""
    CU_G81 = 'G81'
    """Centímetro cúbico por segundo bar"""
    CU_G82 = 'G82'
    """Litro por día bar"""
    CU_G83 = 'G83'
    """Litro por hora bar"""
    CU_G84 = 'G84'
    """Litro por minuto bar"""
    CU_G85 = 'G85'
    """Litro por segundo bar"""
    CU_G86 = 'G86'
    """Metro cúbico por día bar"""
    CU_G87 = 'G87'
    """Metro cúbico por hora bar"""
    CU_G88 = 'G88'
    """Metro cúbico por minuto bar"""
    CU_G89 = 'G89'
    """Metro cúbico por segundo bar"""
    CU_G90 = 'G90'
    """Mililitro por día bar"""
    CU_G91 = 'G91'
    """Mililitro por hora bar"""
    CU_G92 = 'G92'
    """Mililitro por minuto bar"""
    CU_G93 = 'G93'
    """Mililitro por segundo bar"""
    CU_G94 = 'G94'
    """Centímetro cúbico por bar"""
    CU_G95 = 'G95'
    """Litro por bar"""
    CU_G96 = 'G96'
    """Metro cúbico por bar"""
    CU_G97 = 'G97'
    """Mililitro por bar"""
    CU_G98 = 'G98'
    """Micro henry por kiloOhm"""
    CU_G99 = 'G99'
    """Micro henry por Ohm"""
    CU_GB = 'GB'
    """Galón (EUA) por día"""
    CU_GBQ = 'GBQ'
    """Gigabecquerel"""
    CU_GC = 'GC'
    """Gramo por 100 gramos"""
    CU_Gd = 'Gd'
    """Barril bruto"""
    CU_GDW = 'GDW'
    """Gramo, peso seco"""
    CU_GE = 'GE'
    """Libra por galón (EUA)"""
    CU_GF = 'GF'
    """Gramo por metro (gramo por 100 centímetros)"""
    CU_GFI = 'GFI'
    """Gramo de isótopo fisible"""
    CU_GGR = 'GGR'
    """Grandioso"""
    CU_GH = 'GH'
    """Medio galón (US)"""
    CU_GIA = 'GIA'
    """Gill (us)"""
    CU_GIC = 'GIC'
    """Gramo, incluido el contenedor"""
    CU_GII = 'GII'
    """Gill (uk)"""
    CU_GIP = 'GIP'
    """Grama, incluido el embalaje interior"""
    CU_GJ = 'GJ'
    """Gramo por mililitro"""
    CU_GK = 'GK'
    """Gramo por kilogramo"""
    CU_GL = 'GL'
    """Gramo por litro"""
    CU_GLD = 'GLD'
    """Galón seco (EUA)"""
    CU_GLI = 'GLI'
    """Galón (UK)"""
    CU_GLL = 'GLL'
    """Galón (EUA)"""
    CU_GM = 'GM'
    """Gramo por metro cuadrado"""
    CU_GN = 'GN'
    """Galón bruto"""
    CU_GO = 'GO'
    """Miligramo por metro cuadrado"""
    CU_GP = 'GP'
    """Miligramo por metro cúbico"""
    CU_GQ = 'GQ'
    """Microgramo por metro cúbico"""
    CU_GRM = 'GRM'
    """Gramo"""
    CU_GRN = 'GRN'
    """Grano"""
    CU_GRO = 'GRO'
    """Gross"""
    CU_GT = 'GT'
    """Tonelada bruta"""
    CU_GV = 'GV'
    """Gigajoule"""
    CU_GW = 'GW'
    """Galón por mil pies cúbicos"""
    CU_GWH = 'GWH'
    """Gigawatt hora"""
    CU_GY = 'GY'
    """Patio grueso"""
    CU_GZ = 'GZ'
    """Sistema de calibración"""
    CU_H03 = 'H03'
    """Henry por kiloOhm"""
    CU_H04 = 'H04'
    """Henry por Ohm"""
    CU_H05 = 'H05'
    """Milihenry por kiloOhm"""
    CU_H06 = 'H06'
    """Milihenry por Ohm"""
    CU_H07 = 'H07'
    """Pascal segundo por bar"""
    CU_H08 = 'H08'
    """Microbequerel"""
    CU_H09 = 'H09'
    """Año recíproco"""
    CU_H1 = 'H1'
    """Media página - electrónica"""
    CU_H10 = 'H10'
    """Hora recíproca"""
    CU_H11 = 'H11'
    """Mes recíproco"""
    CU_H12 = 'H12'
    """Grado celsius por hora"""
    CU_H13 = 'H13'
    """Grado celsius por minuto"""
    CU_H14 = 'H14'
    """Grado celsius por segundo"""
    CU_H15 = 'H15'
    """Centímetro cuadrado por gramo"""
    CU_H16 = 'H16'
    """Decámetro cuadrado"""
    CU_H18 = 'H18'
    """Hectómetro cuadrado"""
    CU_H19 = 'H19'
    """Hectómetro cúbico"""
    CU_H2 = 'H2'
    """Medio litro"""
    CU_H20 = 'H20'
    """Kilómetro cúbico"""
    CU_H21 = 'H21'
    """Blanco"""
    CU_H22 = 'H22'
    """Voltio pulgada cuadrada por libra fuerza"""
    CU_H23 = 'H23'
    """Voltio por pulgada"""
    CU_H24 = 'H24'
    """Voltio por microsegundo"""
    CU_H25 = 'H25'
    """Por ciento por kelvin"""
    CU_H26 = 'H26'
    """Ohm por metro"""
    CU_H27 = 'H27'
    """Grado por metro"""
    CU_H28 = 'H28'
    """Microfaradio por kilómetro"""
    CU_H29 = 'H29'
    """Microgramo por litro"""
    CU_H30 = 'H30'
    """Micrómetro cuadrado"""
    CU_H31 = 'H31'
    """Amperio por kilogramo"""
    CU_H32 = 'H32'
    """Amperio cuadrado segundo"""
    CU_H33 = 'H33'
    """Faradio por kilómetro"""
    CU_H34 = 'H34'
    """Hertz metro"""
    CU_H35 = 'H35'
    """Kelvin metro por watt"""
    CU_H36 = 'H36'
    """MegaOhm por kilómetro"""
    CU_H37 = 'H37'
    """MegaOhm por metro"""
    CU_H38 = 'H38'
    """Megaamperio"""
    CU_H39 = 'H39'
    """Megahertz kilómetro"""
    CU_H40 = 'H40'
    """Newton por amperio"""
    CU_H41 = 'H41'
    """Newton metro watts elevado a la potencia menos 0.5"""
    CU_H42 = 'H42'
    """Pascal por metro"""
    CU_H43 = 'H43'
    """Siemens por centímetro"""
    CU_H44 = 'H44'
    """TeraOhm"""
    CU_H45 = 'H45'
    """Voltio segundo por metro"""
    CU_H46 = 'H46'
    """Voltio por segundo"""
    CU_H47 = 'H47'
    """Watt por metro cúbico"""
    CU_H48 = 'H48'
    """Attofarad"""
    CU_H49 = 'H49'
    """Centímetro por hora"""
    CU_H50 = 'H50'
    """Reciprocidad del centímetro cúbico"""
    CU_H51 = 'H51'
    """Decibel per kilometro"""
    CU_H52 = 'H52'
    """Decibel per metro"""
    CU_H53 = 'H53'
    """Kilogramo por bar"""
    CU_H54 = 'H54'
    """Kilogramo por decímetro cúbico kelvin"""
    CU_H55 = 'H55'
    """Kilogramo por decímetro cúbico bar"""
    CU_H56 = 'H56'
    """Kilogramo por metro cuadrado segundo"""
    CU_H57 = 'H57'
    """Pulgada por dos pi por radián"""
    CU_H58 = 'H58'
    """Metro por voltio segundo"""
    CU_H59 = 'H59'
    """Metro cuadrado por newton"""
    CU_H60 = 'H60'
    """Metro cúbico por metro cúbico"""
    CU_H61 = 'H61'
    """Milisiemens por centímetro"""
    CU_H62 = 'H62'
    """Milivoltio por minuto"""
    CU_H63 = 'H63'
    """Miligramo por centímetro cuadrado"""
    CU_H64 = 'H64'
    """Miligramo por gramo"""
    CU_H65 = 'H65'
    """Mililitro por metro cúbico"""
    CU_H66 = 'H66'
    """Milímetro por año"""
    CU_H67 = 'H67'
    """Milímetro por hora"""
    CU_H68 = 'H68'
    """MiliMol por gram"""
    CU_H69 = 'H69'
    """Picopascal por kilometro"""
    CU_H70 = 'H70'
    """Picosegundo"""
    CU_H71 = 'H71'
    """Por ciento al mes"""
    CU_H72 = 'H72'
    """Por ciento por hectobar"""
    CU_H73 = 'H73'
    """Por ciento por decakelvin"""
    CU_H74 = 'H74'
    """Watt por metro"""
    CU_H75 = 'H75'
    """Decapascal"""
    CU_H76 = 'H76'
    """Gramo por milímetro"""
    CU_H77 = 'H77'
    """Anchura del módulo"""
    CU_H78 = 'H78'
    """Centímetro convencional de agua"""
    CU_H79 = 'H79'
    """Escala francesa"""
    CU_H80 = 'H80'
    """Unidad de bastidor"""
    CU_H81 = 'H81'
    """Milímetro por minuto"""
    CU_H82 = 'H82'
    """Punto grande"""
    CU_H83 = 'H83'
    """Litro por kilogramo"""
    CU_H84 = 'H84'
    """Gramos milímetro"""
    CU_H85 = 'H85'
    """Semana recíproca"""
    CU_H87 = 'H87'
    """Pieza"""
    CU_H88 = 'H88'
    """MegaOhm kilómetro"""
    CU_H89 = 'H89'
    """Por ciento por Ohmio"""
    CU_H90 = 'H90'
    """Porcentaje por grado"""
    CU_H91 = 'H91'
    """Por ciento por cada diez mil"""
    CU_H92 = 'H92'
    """Ciento por cien mil"""
    CU_H93 = 'H93'
    """Porcentaje por cien"""
    CU_H94 = 'H94'
    """Por ciento por mil"""
    CU_H95 = 'H95'
    """Por ciento por voltio"""
    CU_H96 = 'H96'
    """Tanto por ciento por bar"""
    CU_H98 = 'H98'
    """Por ciento por pulgada"""
    CU_H99 = 'H99'
    """Por ciento por metro"""
    CU_HA = 'HA'
    """Madeja"""
    CU_HAR = 'HAR'
    """hectárea"""
    CU_HBA = 'HBA'
    """Hectobar"""
    CU_HBX = 'HBX'
    """Ciento de cajas"""
    CU_HC = 'HC'
    """Conteo en cientos"""
    CU_HD = 'HD'
    """Media docena"""
    CU_HDW = 'HDW'
    """Cien kilogramos, peso seco"""
    CU_HE = 'HE'
    """Centésima de un quilate"""
    CU_HEA = 'HEA'
    """Cabeza"""
    CU_HF = 'HF'
    """Cien pies"""
    CU_HGM = 'HGM'
    """Hectogramo"""
    CU_HH = 'HH'
    """Cien pies cúbicos"""
    CU_HI = 'HI'
    """Cien hojas"""
    CU_HIU = 'HIU'
    """Unidad internacional de cien"""
    CU_HJ = 'HJ'
    """Potencia métrica"""
    CU_HK = 'HK'
    """Cien kilogramos"""
    CU_HKM = 'HKM'
    """Cien kilogramos, masa neta"""
    CU_HL = 'HL'
    """Cien pies (lineal)"""
    CU_HLT = 'HLT'
    """Hectolitro"""
    CU_HM = 'HM'
    """Milla por hora (milla estatal)"""
    CU_HMQ = 'HMQ'
    """Millones de metros cúbicos"""
    CU_HMT = 'HMT'
    """Hectómetro"""
    CU_HN = 'HN'
    """Milímetro convencional de mercurio"""
    CU_HO = 'HO'
    """Cien onzas troy"""
    CU_HP = 'HP'
    """Milímetro convencional de agua"""
    CU_HPA = 'HPA'
    """Hectolitro de alcohol puro"""
    CU_HS = 'HS'
    """Cien pies cuadrados"""
    CU_HT = 'HT'
    """media hora"""
    CU_HTZ = 'HTZ'
    """Hertz"""
    CU_HUR = 'HUR'
    """Hora"""
    CU_HY = 'HY'
    """Cien yardas"""
    CU_IA = 'IA'
    """Pulgada libra"""
    CU_IC = 'IC'
    """Contar por pulgada"""
    CU_IE = 'IE'
    """Personas"""
    CU_IF = 'IF'
    """Pulgadas de agua"""
    CU_II = 'II'
    """Columna pulgada"""
    CU_IM = 'IM'
    """Impresión"""
    CU_INH = 'INH'
    """Pulgada"""
    CU_INK = 'INK'
    """Pulgada cuadrada"""
    CU_INQ = 'INQ'
    """Pulgada cúbica"""
    CU_IP = 'IP'
    """póliza de seguros"""
    CU_ISD = 'ISD'
    """Grado internacional de azúcar"""
    CU_IT = 'IT'
    """Recuento por centímetro"""
    CU_IU = 'IU'
    """Pulgada por segundo"""
    CU_IV = 'IV'
    """Pulgada por segundo al cuadrado"""
    CU_J10 = 'J10'
    """Por ciento por milímetro"""
    CU_J12 = 'J12'
    """Por mille por psi"""
    CU_J13 = 'J13'
    """Grado api"""
    CU_J14 = 'J14'
    """Grado baume (escala de origen)"""
    CU_J15 = 'J15'
    """Grado baume (us pesado)"""
    CU_J16 = 'J16'
    """Grado baume (luz de los EUA)"""
    CU_J17 = 'J17'
    """Grado balling"""
    CU_J18 = 'J18'
    """Grado brix"""
    CU_J19 = 'J19'
    """Grado fahrenheit hora pie cuadrado por unidad térmica británica (termoquímico)."""
    CU_J2 = 'J2'
    """Joule por kilogramo"""
    CU_J20 = 'J20'
    """Grado fahrenheit por kelvin"""
    CU_J21 = 'J21'
    """Grado fahrenheit por bar"""
    CU_J22 = 'J22'
    """Grado fahrenheit hora pie cuadrado por unidad térmica británica (tabla internacional)."""
    CU_J23 = 'J23'
    """Grado fahrenheit por hora"""
    CU_J24 = 'J24'
    """Grado fahrenheit por minuto"""
    CU_J25 = 'J25'
    """Grado fahrenheit por segundo"""
    CU_J26 = 'J26'
    """Reciprocidad grado fahrenheit"""
    CU_J27 = 'J27'
    """Grado oechsle"""
    CU_J28 = 'J28'
    """Grado rankine por hora"""
    CU_J29 = 'J29'
    """Grado rankine por minuto"""
    CU_J30 = 'J30'
    """Grado rankine por segundo"""
    CU_J31 = 'J31'
    """Grado twaddel."""
    CU_J32 = 'J32'
    """Micropoise"""
    CU_J33 = 'J33'
    """Microgramo por kilogramo"""
    CU_J34 = 'J34'
    """Microgramo por metro cúbico kelvin"""
    CU_J35 = 'J35'
    """Microgramo por metro cúbico bar"""
    CU_J36 = 'J36'
    """Microlitro por litro"""
    CU_J38 = 'J38'
    """Baud"""
    CU_J39 = 'J39'
    """Unidad térmica británica (significado)"""
    CU_J40 = 'J40'
    """Unidad térmica británica (tabla internacional) pie por hora pie cuadrado grado fahrenheit."""
    CU_J41 = 'J41'
    """Unidad térmica británica (tabla internacional) pulgada por hora pie cuadrado grado fahrenheit."""
    CU_J42 = 'J42'
    """Unidad térmica británica (tabla internacional) pulgada por segundo pie cuadrado grado fahrenheit."""
    CU_J43 = 'J43'
    """Unidad térmica británica (tabla internacional) por libra grado fahrenheit"""
    CU_J44 = 'J44'
    """Unidad térmica británica (tabla internacional) por minuto"""
    CU_J45 = 'J45'
    """Unidad térmica británica (tabla internacional) por segundo"""
    CU_J46 = 'J46'
    """Unidad térmica británica (termoquímico) pie por hora pie cuadrado grado fahrenheit."""
    CU_J47 = 'J47'
    """Unidad térmica británica (termoquímica) por hora"""
    CU_J48 = 'J48'
    """Unidad térmica británica (termoquímico) pulgada por hora pie cuadrado grado fahrenheit."""
    CU_J49 = 'J49'
    """Unidad térmica británica (termoquímico) pulgada por segundo pie cuadrado grado fahrenheit."""
    CU_J50 = 'J50'
    """Unidad térmica británica (termoquímico) por libra grado fahrenheit"""
    CU_J51 = 'J51'
    """Unidad térmica británica (termoquímica) por minuto"""
    CU_J52 = 'J52'
    """Unidad térmica británica (termoquímica) por segundo"""
    CU_J53 = 'J53'
    """Culombio metro cuadrado por kilogramo"""
    CU_J54 = 'J54'
    """Megabaud"""
    CU_J55 = 'J55'
    """Watt segundo"""
    CU_J56 = 'J56'
    """Bar por bar"""
    CU_J57 = 'J57'
    """Barril (uk petróleo)"""
    CU_J58 = 'J58'
    """Barril (petróleo UK) por minuto"""
    CU_J59 = 'J59'
    """Barril (petróleo UK) por día"""
    CU_J60 = 'J60'
    """Barril (petróleo UK) por hora"""
    CU_J61 = 'J61'
    """Barril (petróleo UK) por segundo"""
    CU_J62 = 'J62'
    """Barril (petróleo estados unidos) por hora"""
    CU_J63 = 'J63'
    """Barril (petróleo estados unidos) por segundo"""
    CU_J64 = 'J64'
    """Bushel (UK) por día"""
    CU_J65 = 'J65'
    """Bushel (UK) por hora"""
    CU_J66 = 'J66'
    """Bushel (UK) por minuto"""
    CU_J67 = 'J67'
    """Bushel (UK) por segundo"""
    CU_J68 = 'J68'
    """Bushel (seco, estados unidos) por día"""
    CU_J69 = 'J69'
    """Bushel (seco, estados unidos) por hora"""
    CU_J70 = 'J70'
    """Bushel (seco, estados unidos) por minuto"""
    CU_J71 = 'J71'
    """Bushel (seco, estados unidos) por segundo"""
    CU_J72 = 'J72'
    """Centinewton metro"""
    CU_J73 = 'J73'
    """Centipoise por kelvin"""
    CU_J74 = 'J74'
    """Centipoise por bar"""
    CU_J75 = 'J75'
    """Caloría"""
    CU_J76 = 'J76'
    """Caloría (tabla internacional) por gramo grado celsius"""
    CU_J78 = 'J78'
    """Caloría (termoquímica) por centímetro segundo grado celsius"""
    CU_J79 = 'J79'
    """Caloría (termoquímico) por gramo grado celsius"""
    CU_J81 = 'J81'
    """Caloría (termoquímica) por minuto"""
    CU_J82 = 'J82'
    """Caloría (termoquímica) por segundo"""
    CU_J83 = 'J83'
    """Clo"""
    CU_J84 = 'J84'
    """Centímetro por segundo kelvin"""
    CU_J85 = 'J85'
    """Centímetro por segundo bar"""
    CU_J87 = 'J87'
    """Centímetro cúbico por metro cúbico"""
    CU_J89 = 'J89'
    """Centímetro de mercurio"""
    CU_J90 = 'J90'
    """Decímetro cúbico por día"""
    CU_J91 = 'J91'
    """Decímetro cúbico por metro cúbico"""
    CU_J92 = 'J92'
    """Decímetro cúbico por minuto"""
    CU_J93 = 'J93'
    """Decímetro cúbico por segundo"""
    CU_J94 = 'J94'
    """Dina centímetro"""
    CU_J95 = 'J95'
    """Onza (fluido, UK) por día"""
    CU_J96 = 'J96'
    """Onza (fluido, UK) por hora"""
    CU_J97 = 'J97'
    """Onza (fluido, UK) por minuto"""
    CU_J98 = 'J98'
    """Onza (fluido, UK) por segundo"""
    CU_J99 = 'J99'
    """Onza (fluido, estados unidos) por día"""
    CU_JB = 'JB'
    """Jumbo"""
    CU_JE = 'JE'
    """Joule por kelvin"""
    CU_JK = 'JK'
    """Megajoule por kilogramo"""
    CU_JM = 'JM'
    """Megajoule por metro cúbico"""
    CU_JNT = 'JNT'
    """Junta de tubería"""
    CU_Jo = 'Jo'
    """Articulación"""
    CU_JOU = 'JOU'
    """Joule"""
    CU_JPS = 'JPS'
    """Cien metros"""
    CU_JWL = 'JWL'
    """Número de joyas"""
    CU_K1 = 'K1'
    """Demanda de kilowatt"""
    CU_K10 = 'K10'
    """Onza (fluido, estados unidos) por hora"""
    CU_K11 = 'K11'
    """Onza (fluido, estados unidos) por minuto"""
    CU_K12 = 'K12'
    """Onza (fluido, estados unidos) por segundo"""
    CU_K13 = 'K13'
    """Pie por grado fahrenheit"""
    CU_K14 = 'K14'
    """Pie por hora"""
    CU_K15 = 'K15'
    """Pie libra-fuerza por hora"""
    CU_K16 = 'K16'
    """Pie libra-fuerza por minuto"""
    CU_K17 = 'K17'
    """Pie por psi (libra por pulgada cuadrada)"""
    CU_K18 = 'K18'
    """Pie por segundo grado fahrenheit"""
    CU_K19 = 'K19'
    """Pie por segundo psi (libra por pulgada cuadrada)"""
    CU_K2 = 'K2'
    """Kilovoltios amperios demanda reactiva"""
    CU_K20 = 'K20'
    """Reciprocidad del pie cuadrado"""
    CU_K21 = 'K21'
    """Pie cúbico por grado fahrenheit"""
    CU_K22 = 'K22'
    """Pie cúbico por día"""
    CU_K23 = 'K23'
    """Pie cúbico por psi (libra por pulgada cuadrada)"""
    CU_K24 = 'K24'
    """Pie de agua"""
    CU_K25 = 'K25'
    """Pie de mercurio"""
    CU_K26 = 'K26'
    """Galón (UK) por día"""
    CU_K27 = 'K27'
    """Galón (UK) por hora"""
    CU_K28 = 'K28'
    """Galón (UK) por segundo"""
    CU_K3 = 'K3'
    """Kilovoltio amperio hora reactivo"""
    CU_K30 = 'K30'
    """Galón (líquido, EUA) por segundo"""
    CU_K31 = 'K31'
    """Gramo-fuerza por centímetro cuadrado"""
    CU_K32 = 'K32'
    """Gill (UK) por día"""
    CU_K33 = 'K33'
    """Gill (UK) por hora"""
    CU_K34 = 'K34'
    """Gill (UK) por minuto"""
    CU_K35 = 'K35'
    """Gill (UK) por segundo"""
    CU_K36 = 'K36'
    """Gill (estados unidos) por día"""
    CU_K37 = 'K37'
    """Gill (estados unidos) por hora"""
    CU_K38 = 'K38'
    """Gill (estados unidos) por minuto"""
    CU_K39 = 'K39'
    """Gill (estados unidos) por segundo"""
    CU_K40 = 'K40'
    """Aceleración estándar de la caída libre"""
    CU_K41 = 'K41'
    """Grano por galón (EUA)"""
    CU_K42 = 'K42'
    """Caballo de fuerza de caldera"""
    CU_K43 = 'K43'
    """Caballo de fuerza (eléctrico)"""
    CU_K45 = 'K45'
    """Pulgada por grado fahrenheit"""
    CU_K46 = 'K46'
    """Pulgada por psi (libra por pulgada cuadrada)"""
    CU_K47 = 'K47'
    """Pulgada por segundo grado fahrenheit"""
    CU_K48 = 'K48'
    """Pulgada por segundo psi (libra por pulgada cuadrada)"""
    CU_K49 = 'K49'
    """Reciprocidad de la pulgada cuadrada"""
    CU_K5 = 'K5'
    """Kilovoltios amperios (reactivos)"""
    CU_K50 = 'K50'
    """Kilobaud"""
    CU_K51 = 'K51'
    """Kilocaloría (significado)"""
    CU_K52 = 'K52'
    """Kilocaloría (tabla internacional) por hora metro grado celsius"""
    CU_K53 = 'K53'
    """Kilocaloría (termoquímico)"""
    CU_K54 = 'K54'
    """Kilocaloría (termoquímica) por minuto"""
    CU_K55 = 'K55'
    """Kilocaloría (termoquímica) por segundo"""
    CU_K58 = 'K58'
    """KiloMol por hora"""
    CU_K59 = 'K59'
    """KiloMol por metro cúbico kelvin"""
    CU_K6 = 'K6'
    """Kilolitro"""
    CU_K60 = 'K60'
    """KiloMol por metro cúbico bar"""
    CU_K61 = 'K61'
    """KiloMol por minuto"""
    CU_K62 = 'K62'
    """Litro por litro"""
    CU_K63 = 'K63'
    """Reciprocidad del litro"""
    CU_K64 = 'K64'
    """Libra (avoirdupois) por grado fahrenheit"""
    CU_K65 = 'K65'
    """Libra (avoirdupois) pie cuadrado"""
    CU_K66 = 'K66'
    """Libra (avoirdupois) por día"""
    CU_K67 = 'K67'
    """Libra por pie hora"""
    CU_K68 = 'K68'
    """Libra por pie segundo"""
    CU_K69 = 'K69'
    """Libra (avoirdupois) por pie cúbico grado fahrenheit"""
    CU_K70 = 'K70'
    """Libra (avoirdupois) por pie cúbico psi"""
    CU_K71 = 'K71'
    """Libra (avoirdupois) por galón (UK)"""
    CU_K73 = 'K73'
    """Libra (avoirdupois) por hora grados fahrenheit"""
    CU_K74 = 'K74'
    """Libra (avoirdupois) por hora libra-fuerza por pulgada cuadrada"""
    CU_K75 = 'K75'
    """Libra (avoirdupois) por pulgada cúbica grado fahrenheit"""
    CU_K76 = 'K76'
    """Libra (avoirdupois) por pulgada cúbica psi"""
    CU_K77 = 'K77'
    """Libra (avoirdupois) por psi"""
    CU_K78 = 'K78'
    """Libra (avoirdupois) por minuto"""
    CU_K79 = 'K79'
    """Libra (avoirdupois) por minuto grados fahrenheit"""
    CU_K80 = 'K80'
    """Libra (avoirdupois) por minuto libra-fuerza por pulgada cuadrada"""
    CU_K81 = 'K81'
    """Libra (avoirdupois) por segundo"""
    CU_K82 = 'K82'
    """Libra (avoirdupois)por segundo grados fahrenheit"""
    CU_K83 = 'K83'
    """Libra (avoirdupois) por segundo libra-fuerza por pulgada cuadrada"""
    CU_K84 = 'K84'
    """Libra por yarda cúbica"""
    CU_K85 = 'K85'
    """Libra-fuerza por pie cuadrado"""
    CU_K86 = 'K86'
    """Libra-fuerza por pulgada cuadrada grados fahrenheit"""
    CU_K87 = 'K87'
    """Libra-fuerza por pulgada cuadrada pulgada cúbica por segundo"""
    CU_K88 = 'K88'
    """Libra-fuerza por pulgada cuadrada litro por segundo"""
    CU_K89 = 'K89'
    """Libra-fuerza por pulgada cuadrada metro cúbico por segundo"""
    CU_K90 = 'K90'
    """Libra-fuerza por pulgada cuadrada yarda cúbica por segundo"""
    CU_K91 = 'K91'
    """Libra-fuerza segundo por pie cuadrado"""
    CU_K92 = 'K92'
    """Libra-fuerza segundo por pulgada cuadrada"""
    CU_K93 = 'K93'
    """Reciprocidad psi"""
    CU_K94 = 'K94'
    """Cuarto (líquido, UK) por día"""
    CU_K95 = 'K95'
    """Cuarto (líquido, UK) por hora"""
    CU_K96 = 'K96'
    """Cuarto (líquido, UK) por minuto"""
    CU_K97 = 'K97'
    """Cuarto (líquido, UK) por segundo"""
    CU_K98 = 'K98'
    """Cuarto (líquido, estados unidos) por día"""
    CU_K99 = 'K99'
    """Cuarto (líquido, estados unidos) por hora"""
    CU_KA = 'KA'
    """Pastel"""
    CU_KAT = 'KAT'
    """Katal"""
    CU_KB = 'KB'
    """Kilocaracter"""
    CU_KBA = 'KBA'
    """Kilobar"""
    CU_KCC = 'KCC'
    """Kilogramo de cloruro de colina"""
    CU_KD = 'KD'
    """Kilogram decimal"""
    CU_KDW = 'KDW'
    """Kilogramo de peso neto drenado"""
    CU_KEL = 'KEL'
    """Kelvin"""
    CU_KF = 'KF'
    """Kilopacket"""
    CU_KGM = 'KGM'
    """Kilogramo"""
    CU_KGS = 'KGS'
    """Kilogramo por segundo"""
    CU_KHY = 'KHY'
    """Kilogramo de peróxido de hidrógeno"""
    CU_KHZ = 'KHZ'
    """Kilohertz"""
    CU_KI = 'KI'
    """Kilogramo por milímetro de ancho"""
    CU_KIC = 'KIC'
    """Kilogramo, incluyendo el contenedor"""
    CU_KIP = 'KIP'
    """Kilogramo, incluyendo el empaquetado interno"""
    CU_KJ = 'KJ'
    """Kilosegmento"""
    CU_KJO = 'KJO'
    """Kilojoule"""
    CU_KL = 'KL'
    """Kilogramo por metro"""
    CU_KLK = 'KLK'
    """Porcentaje de material seco láctico"""
    CU_KLX = 'KLX'
    """Kilolux"""
    CU_KMA = 'KMA'
    """Kilogramo de metilamina"""
    CU_KMH = 'KMH'
    """Kilómetro por hora"""
    CU_KMK = 'KMK'
    """Kilómetro cuadrado"""
    CU_KMQ = 'KMQ'
    """Kilogramo por metro cúbico"""
    CU_KMT = 'KMT'
    """Kilómetro"""
    CU_KNI = 'KNI'
    """Kilogramo de nitrógeno"""
    CU_KNM = 'KNM'
    """Kolonewton por metro cuadrado"""
    CU_KNS = 'KNS'
    """Kilogramo sustancia nombrada"""
    CU_KNT = 'KNT'
    """Nudo"""
    CU_KO = 'KO'
    """Miliequivalentes de potasa cáustica por gramo de producto"""
    CU_KPA = 'KPA'
    """Kilopascal"""
    CU_KPH = 'KPH'
    """Kilogramo de hidróxido de potasio (potasa cáustica)"""
    CU_KPO = 'KPO'
    """Kilogramo de óxido de potasio"""
    CU_KPP = 'KPP'
    """Kilogramo de pentóxido de fósforo (anhídrido fosfórico)"""
    CU_KR = 'KR'
    """Kiloroentgen"""
    CU_KS = 'KS'
    """Mil libras por pulgada cuadrada"""
    CU_KSD = 'KSD'
    """Kilogramo de sustancia 90% seco"""
    CU_KSH = 'KSH'
    """Kilogramo de hidróxido de sodio (sodio cáustica)"""
    CU_KT = 'KT'
    """Kit"""
    CU_KTN = 'KTN'
    """Kilotonelada Métrica"""
    CU_KUR = 'KUR'
    """Kilogramo de uranio"""
    CU_KVA = 'KVA'
    """Kilovoltio - amperio"""
    CU_KVR = 'KVR'
    """Kilovar"""
    CU_KVT = 'KVT'
    """Kilovoltio"""
    CU_KW = 'KW'
    """Kilogramo por milímetro"""
    CU_KWH = 'KWH'
    """Kilowatt hora"""
    CU_KWN = 'KWN'
    """Kilowatt hora por metro cúbico normalizado"""
    CU_KWO = 'KWO'
    """Kilogramo de trióxido de tungsteno"""
    CU_KWS = 'KWS'
    """Kilowatt hora por metro cúbico estándar"""
    CU_KWT = 'KWT'
    """Kilowatt"""
    CU_KX = 'KX'
    """Mililitro por kilogramo"""
    CU_L10 = 'L10'
    """Cuarto (líquido, estados unidos) por minuto"""
    CU_L11 = 'L11'
    """Cuarto (líquido, estados unidos) por segundo"""
    CU_L12 = 'L12'
    """Metro por segundo kelvin"""
    CU_L13 = 'L13'
    """Metro por segundo bar"""
    CU_L14 = 'L14'
    """Metro cuadrado hora grado celsius por kilocaloría (tabla internacional)"""
    CU_L15 = 'L15'
    """Milipascal segundo por kelvin"""
    CU_L16 = 'L16'
    """Milipascal segundo por bar"""
    CU_L17 = 'L17'
    """Miligramo por metro cúbico kelvin"""
    CU_L18 = 'L18'
    """Miligramo por metro cúbico bar"""
    CU_L19 = 'L19'
    """Mililitro por litro"""
    CU_L2 = 'L2'
    """Litro por minuto"""
    CU_L20 = 'L20'
    """Reciprocidad del milímetro cúbico"""
    CU_L21 = 'L21'
    """Milímetro cúbico por metro cúbico"""
    CU_L23 = 'L23'
    """Mol por hora"""
    CU_L24 = 'L24'
    """Mol por kilogramo kelvin"""
    CU_L25 = 'L25'
    """Mol por kilogramo bar"""
    CU_L26 = 'L26'
    """Mol por litro kelvin"""
    CU_L27 = 'L27'
    """Mol por litro bar"""
    CU_L28 = 'L28'
    """Mol por metro cúbico kelvin"""
    CU_L29 = 'L29'
    """Mol por metro cúbico bar"""
    CU_L30 = 'L30'
    """Mol por minuto"""
    CU_L31 = 'L31'
    """Milliroentgen aequivalent men"""
    CU_L32 = 'L32'
    """Nanogramo por kilogramo"""
    CU_L33 = 'L33'
    """Onza (avoirdupois) por día"""
    CU_L34 = 'L34'
    """Onza (avoirdupois) por hora"""
    CU_L35 = 'L35'
    """Onza (avoirdupois) por minuto"""
    CU_L36 = 'L36'
    """Onza (avoirdupois) por segundo"""
    CU_L37 = 'L37'
    """Onza (avoirdupois) por galón (UK)"""
    CU_L38 = 'L38'
    """Onza (avoirdupois) por galón (EUA)"""
    CU_L39 = 'L39'
    """Onza (avoirdupois) por pulgada cúbica"""
    CU_L40 = 'L40'
    """Onza fuerza"""
    CU_L41 = 'L41'
    """Onza (avoirdupois) fuerza pulgada"""
    CU_L42 = 'L42'
    """Picosiemens por metro"""
    CU_L43 = 'L43'
    """Peck (UK)"""
    CU_L44 = 'L44'
    """Peck (UK) por día"""
    CU_L45 = 'L45'
    """Peck (UK) por hora"""
    CU_L46 = 'L46'
    """Peck (UK) por minuto"""
    CU_L47 = 'L47'
    """Peck (UK) por segundo"""
    CU_L48 = 'L48'
    """Peck (seco, estados unidos) por día"""
    CU_L49 = 'L49'
    """Peck (seco, estados unidos) por hora"""
    CU_L50 = 'L50'
    """Peck (seco, estados unidos) por minuto"""
    CU_L51 = 'L51'
    """Peck (seco, estados unidos) por segundo"""
    CU_L52 = 'L52'
    """Libra.fuerza por pulgada cuadrada por libra fuerza por pulgada cuadrada"""
    CU_L53 = 'L53'
    """Pinta (UK) por día"""
    CU_L54 = 'L54'
    """Pinta (UK) por hora"""
    CU_L55 = 'L55'
    """Pinta (UK) por minuto"""
    CU_L56 = 'L56'
    """Pinta (UK) por segundo"""
    CU_L57 = 'L57'
    """Pinta (líquido, estados unidos) por día"""
    CU_L58 = 'L58'
    """Pinta (líquido, estados unidos) por hora"""
    CU_L59 = 'L59'
    """Pinta (líquido, estados unidos) por minuto"""
    CU_L60 = 'L60'
    """Pinta (líquido, estados unidos) por segundo"""
    CU_L61 = 'L61'
    """Pinta (US seco)"""
    CU_L62 = 'L62'
    """Cuarto de galón (seco de los EUA)"""
    CU_L63 = 'L63'
    """Slug por día"""
    CU_L64 = 'L64'
    """Slug por pie segundo"""
    CU_L65 = 'L65'
    """Slug por pie cúbico"""
    CU_L66 = 'L66'
    """Slug por hora"""
    CU_L67 = 'L67'
    """Slug por minuto"""
    CU_L68 = 'L68'
    """Slug por segundo"""
    CU_L69 = 'L69'
    """Tonelada por kelvin"""
    CU_L70 = 'L70'
    """Tonelada por bar"""
    CU_L71 = 'L71'
    """Tonelada por día"""
    CU_L72 = 'L72'
    """Tonelada por día kelvin"""
    CU_L73 = 'L73'
    """Tonelada por día bar"""
    CU_L74 = 'L74'
    """Tonelada por hora kelvin"""
    CU_L75 = 'L75'
    """Tonelada por hora bar"""
    CU_L76 = 'L76'
    """Tonelada por metro cúbico kelvin"""
    CU_L77 = 'L77'
    """Tonelada por metro cúbico bar"""
    CU_L78 = 'L78'
    """Tonelada por minuto"""
    CU_L79 = 'L79'
    """Tonelada por minuto kelvin"""
    CU_L80 = 'L80'
    """Tonelada por minuto bar"""
    CU_L81 = 'L81'
    """Tonelada por segundo"""
    CU_L82 = 'L82'
    """Tonelada por segundo kelvin"""
    CU_L83 = 'L83'
    """Tonelada por segundo bar"""
    CU_L84 = 'L84'
    """Tonelada (flota UK)"""
    CU_L85 = 'L85'
    """Tonelada larga por día"""
    CU_L86 = 'L86'
    """Tonelada (flota estados unidos)"""
    CU_L87 = 'L87'
    """Tonelada corta por grado fahrenheit"""
    CU_L88 = 'L88'
    """Tonelada corta por día"""
    CU_L89 = 'L89'
    """Tonelada corta por hora grados fahrenheit"""
    CU_L90 = 'L90'
    """Tonelada corta por hora libra-fuerza por pulgada cuadrada"""
    CU_L91 = 'L91'
    """Tonelada corta por psi"""
    CU_L92 = 'L92'
    """Tonelada larga (UK) por yarda cúbica"""
    CU_L93 = 'L93'
    """Tonelada corta (estados unidos) por yarda cúbica"""
    CU_L94 = 'L94'
    """Tonelada fuerza"""
    CU_L95 = 'L95'
    """Año común"""
    CU_L96 = 'L96'
    """Año sideral"""
    CU_L98 = 'L98'
    """Yarda por grado fahrenheit"""
    CU_L99 = 'L99'
    """Yarda por psi (libra por pulgada cuadrada)"""
    CU_LA = 'LA'
    """Libra por pulgada cúbica"""
    CU_LAC = 'LAC'
    """Porcentaje de exceso de lactosa"""
    CU_LBR = 'LBR'
    """Libra"""
    CU_LBT = 'LBT'
    """Troy pound"""
    CU_LC = 'LC'
    """Centímetro lineal"""
    CU_LD = 'LD'
    """Litro por día"""
    CU_LE = 'LE'
    """Lite"""
    CU_LEF = 'LEF'
    """Hoja"""
    CU_LF = 'LF'
    """Pie lineal"""
    CU_LH = 'LH'
    """Hora de trabajo"""
    CU_LI = 'LI'
    """Pulgada lineal"""
    CU_LJ = 'LJ'
    """Spray grande"""
    CU_LK = 'LK'
    """Enlazar"""
    CU_LM = 'LM'
    """Metro lineal"""
    CU_LN = 'LN'
    """Longitud"""
    CU_LO = 'LO'
    """Lote [unidad de adquisición]"""
    CU_LP = 'LP'
    """Libra líquida"""
    CU_LPA = 'LPA'
    """Litro de alcohol puro"""
    CU_LR = 'LR'
    """Capa"""
    CU_LS = 'LS'
    """Suma global"""
    CU_LTN = 'LTN'
    """Tonelada (UK) o tonelada larga (estados unidos)"""
    CU_LTR = 'LTR'
    """Litro"""
    CU_LUB = 'LUB'
    """Tonelada métrica, aceite lubricante"""
    CU_LUM = 'LUM'
    """Lumen"""
    CU_LUX = 'LUX'
    """Lux"""
    CU_LX = 'LX'
    """Yarda lineal por libra"""
    CU_LY = 'LY'
    """Yarda lineal"""
    CU_M0 = 'M0'
    """cinta magnética"""
    CU_M1 = 'M1'
    """Miligramo por litro"""
    CU_M10 = 'M10'
    """Reciprocidad de la yarda cuadrada"""
    CU_M11 = 'M11'
    """Yarda cúbica por grado fahrenheit"""
    CU_M12 = 'M12'
    """Yarda cúbica por día"""
    CU_M13 = 'M13'
    """Yarda cúbica por hora"""
    CU_M14 = 'M14'
    """Yarda cúbica por psi (libra por pulgada cuadrada)"""
    CU_M15 = 'M15'
    """Yarda cúbica por minuto"""
    CU_M16 = 'M16'
    """Yarda cúbica por segundo"""
    CU_M17 = 'M17'
    """Kilohertz metro"""
    CU_M18 = 'M18'
    """Gigahertz metro"""
    CU_M19 = 'M19'
    """Beaufort"""
    CU_M20 = 'M20'
    """Recíproco de megakelvin o megakelvin a la potencia menos 1"""
    CU_M21 = 'M21'
    """Kilovoltio-amperio hora reciprocidad"""
    CU_M22 = 'M22'
    """Milímetro por centímetro cuadrado minuto"""
    CU_M23 = 'M23'
    """Newton por centímetro"""
    CU_M24 = 'M24'
    """Ohm kilómetro"""
    CU_M25 = 'M25'
    """Porcentaje por grado celsius"""
    CU_M26 = 'M26'
    """GigaOhm por metro"""
    CU_M27 = 'M27'
    """Megahertz metro"""
    CU_M29 = 'M29'
    """Kilogramo por kilogramo"""
    CU_M30 = 'M30'
    """voltio-amperio segundo reciprocidad"""
    CU_M31 = 'M31'
    """Kilogramo por kilómetro"""
    CU_M32 = 'M32'
    """Segundos pascal por litro"""
    CU_M33 = 'M33'
    """MiliMol por litro"""
    CU_M34 = 'M34'
    """Newton metro por metro cuadrado"""
    CU_M35 = 'M35'
    """Milivoltio - amperio"""
    CU_M36 = 'M36'
    """Mes de 30 días"""
    CU_M37 = 'M37'
    """Actual 360"""
    CU_M38 = 'M38'
    """Kilómetro por segundo cuadrado"""
    CU_M39 = 'M39'
    """Centímetro por segundo cuadrado"""
    CU_M4 = 'M4'
    """Valor monetario"""
    CU_M40 = 'M40'
    """Yarda por segundo cuadrado"""
    CU_M41 = 'M41'
    """Milímetro por segundo cuadrado"""
    CU_M42 = 'M42'
    """Milla (milla estatal)  por segundo cuadrado"""
    CU_M43 = 'M43'
    """Mil (unidad de Medida Militar)"""
    CU_M44 = 'M44'
    """Revolución"""
    CU_M45 = 'M45'
    """Grado por segundo cuadrado"""
    CU_M46 = 'M46'
    """Revolución por minuto"""
    CU_M47 = 'M47'
    """Circular Mil"""
    CU_M48 = 'M48'
    """Milla cuadrada (basado en u.s survey foot)"""
    CU_M49 = 'M49'
    """Cadena"""
    CU_M5 = 'M5'
    """Microcurie"""
    CU_M50 = 'M50'
    """Estadio"""
    CU_M51 = 'M51'
    """Pie (Topografía UEA)"""
    CU_M52 = 'M52'
    """Milla"""
    CU_M53 = 'M53'
    """Metro por pascal"""
    CU_M55 = 'M55'
    """Metro por radián"""
    CU_M56 = 'M56'
    """Shake"""
    CU_M57 = 'M57'
    """Milla por minuto"""
    CU_M58 = 'M58'
    """Milla por segundo"""
    CU_M59 = 'M59'
    """Metro por segundo pascal"""
    CU_M60 = 'M60'
    """Metro por hora"""
    CU_M61 = 'M61'
    """Pulgada por año"""
    CU_M62 = 'M62'
    """Kilómetro por segundo"""
    CU_M63 = 'M63'
    """Pulgada por minuto"""
    CU_M64 = 'M64'
    """Yarda por segundo"""
    CU_M65 = 'M65'
    """Yarda por minuto"""
    CU_M66 = 'M66'
    """Yarda por hora"""
    CU_M67 = 'M67'
    """Acre-pie"""
    CU_M68 = 'M68'
    """Cordón"""
    CU_M69 = 'M69'
    """Milla cúbica (reinounido)"""
    CU_M7 = 'M7'
    """Micro-pulgada"""
    CU_M70 = 'M70'
    """Unidad tradicional de capacidad de carga"""
    CU_M71 = 'M71'
    """Metro cúbico por pascal (joules)"""
    CU_M72 = 'M72'
    """Bel"""
    CU_M73 = 'M73'
    """Kilogramo por metro cúbico pascal"""
    CU_M74 = 'M74'
    """Kilogramo por pascal"""
    CU_M75 = 'M75'
    """Kilolibra fuerza"""
    CU_M76 = 'M76'
    """Poundal"""
    CU_M77 = 'M77'
    """Kilogramo metro por segundo cuadrado"""
    CU_M78 = 'M78'
    """Pond"""
    CU_M79 = 'M79'
    """Pie cuadrado por hora"""
    CU_M80 = 'M80'
    """Stokes por pascal"""
    CU_M81 = 'M81'
    """Centímetro cuadrado por segundo"""
    CU_M82 = 'M82'
    """Metro cuadrado por segundo pascal"""
    CU_M83 = 'M83'
    """Denier"""
    CU_M84 = 'M84'
    """Libra por yarda"""
    CU_M85 = 'M85'
    """Tonelada, ensayo"""
    CU_M86 = 'M86'
    """Libra Alemana"""
    CU_M87 = 'M87'
    """Kilogramo por segundo pascal"""
    CU_M88 = 'M88'
    """Tonelada por mes"""
    CU_M89 = 'M89'
    """Tonelada por año"""
    CU_M9 = 'M9'
    """Millones de btu por 1000 pies cúbicos"""
    CU_M90 = 'M90'
    """Kilolibra por hora"""
    CU_M91 = 'M91'
    """Libra por libra"""
    CU_M92 = 'M92'
    """Libra fuerza pie"""
    CU_M93 = 'M93'
    """Newton metro por radián"""
    CU_M94 = 'M94'
    """Kilogramo metro"""
    CU_M95 = 'M95'
    """Poundal pie"""
    CU_M96 = 'M96'
    """Poundal pulgada"""
    CU_M97 = 'M97'
    """Dina metro"""
    CU_M98 = 'M98'
    """Kilogramo centímetro por segundo"""
    CU_M99 = 'M99'
    """Gramo centímetro por segundo"""
    CU_MA = 'MA'
    """Máquina por unidad"""
    CU_MAH = 'MAH'
    """Megavoltio amperio reactivo hora"""
    CU_MAL = 'MAL'
    """Megalitro"""
    CU_MAM = 'MAM'
    """Megametro"""
    CU_MAR = 'MAR'
    """Megavar"""
    CU_MAW = 'MAW'
    """Megawatt"""
    CU_MBE = 'MBE'
    """Mil equivalente de ladrillo estándar"""
    CU_MBF = 'MBF'
    """Mil pies de tabla"""
    CU_MBR = 'MBR'
    """Milibar"""
    CU_MC = 'MC'
    """Microgramo"""
    CU_MCU = 'MCU'
    """Milicurie"""
    CU_MD = 'MD'
    """Tonelada métrica seca al aire"""
    CU_MF = 'MF'
    """Miligramo por pie cuadrado por lado"""
    CU_MGM = 'MGM'
    """Miligramo"""
    CU_MHZ = 'MHZ'
    """Megahertz"""
    CU_MIK = 'MIK'
    """Milla cuadrada (milla estatal)"""
    CU_MIL = 'MIL'
    """Mil"""
    CU_MIN = 'MIN'
    """Minuto [unidad de tiempo]"""
    CU_MIO = 'MIO'
    """Millón"""
    CU_MIU = 'MIU'
    """Unidad internacional de millón"""
    CU_MK = 'MK'
    """Miligramo por pulgada cuadrada"""
    CU_MLD = 'MLD'
    """Mil millones"""
    CU_MLT = 'MLT'
    """Mililitro"""
    CU_MMK = 'MMK'
    """Milímetro cuadrado"""
    CU_MMQ = 'MMQ'
    """Milímetro cúbico"""
    CU_MMT = 'MMT'
    """Milímetro"""
    CU_MND = 'MND'
    """Kilogramo, peso seco"""
    CU_MON = 'MON'
    """Mes"""
    CU_MPA = 'MPA'
    """Megapascal"""
    CU_MQ = 'MQ'
    """Mil metros"""
    CU_MQH = 'MQH'
    """Metro cúbico por hora"""
    CU_MQS = 'MQS'
    """Metro cúbico por segundo"""
    CU_MSK = 'MSK'
    """Metro por segundo cuadrado"""
    CU_MTK = 'MTK'
    """Metro cuadrado"""
    CU_MTQ = 'MTQ'
    """Metro cúbico"""
    CU_MTR = 'MTR'
    """Metro"""
    CU_MTS = 'MTS'
    """Metro por segundo"""
    CU_MV = 'MV'
    """Número de mults"""
    CU_MVA = 'MVA'
    """Megavoltio - amperio"""
    CU_MWH = 'MWH'
    """Megawatt hora"""
    CU_N1 = 'N1'
    """Pluma calórica"""
    CU_N10 = 'N10'
    """Libra pie por segundo"""
    CU_N11 = 'N11'
    """Libra pulgada por segundo"""
    CU_N12 = 'N12'
    """Pferdestaerke"""
    CU_N13 = 'N13'
    """Centímetro de mercurio (0°)"""
    CU_N14 = 'N14'
    """Centímetro de agua (4°)"""
    CU_N15 = 'N15'
    """Pie de agua (39.2 °f)"""
    CU_N16 = 'N16'
    """Pulgada de mercurio (32 °f)"""
    CU_N17 = 'N17'
    """Pulgada de mercurio (60 °f)"""
    CU_N18 = 'N18'
    """Pulgada de agua (39.2 °f)"""
    CU_N19 = 'N19'
    """Pulgada de agua (60 °f)"""
    CU_N2 = 'N2'
    """número de líneas"""
    CU_N20 = 'N20'
    """Kip por pulgada cuadrada"""
    CU_N21 = 'N21'
    """Poundal por pie cuadrado"""
    CU_N22 = 'N22'
    """Onza (avoirdupois) por pulgada cuadrada"""
    CU_N23 = 'N23'
    """Metro convencional de agua"""
    CU_N24 = 'N24'
    """Gramo por milímetro cuadrado"""
    CU_N25 = 'N25'
    """Libra por yarda cuadrada"""
    CU_N26 = 'N26'
    """Poundal por pulgada cuadrada"""
    CU_N27 = 'N27'
    """Pie a la cuarta potencia"""
    CU_N28 = 'N28'
    """Decímetro cúbico por kilogramo"""
    CU_N29 = 'N29'
    """Pie cúbico por libra"""
    CU_N3 = 'N3'
    """Impresión de punto"""
    CU_N30 = 'N30'
    """Pulgada cúbica por libra"""
    CU_N31 = 'N31'
    """Kilonewton por metro"""
    CU_N32 = 'N32'
    """Poundal por pulgada"""
    CU_N33 = 'N33'
    """Libra-fuerza por yarda"""
    CU_N34 = 'N34'
    """Poundal segundo por pie cuadrado"""
    CU_N35 = 'N35'
    """Poise por pascal"""
    CU_N36 = 'N36'
    """Newton segundo por metro cuadrado"""
    CU_N37 = 'N37'
    """Kilogramo por metro segundo"""
    CU_N38 = 'N38'
    """Kilogramo por metro minuto"""
    CU_N39 = 'N39'
    """Kilogramo por metro día"""
    CU_N40 = 'N40'
    """Kilogramo por metro hora"""
    CU_N41 = 'N41'
    """Gramo por centímetro segundo"""
    CU_N42 = 'N42'
    """Poundal segundo por pulgada cuadrada"""
    CU_N43 = 'N43'
    """Libra por pie minuto"""
    CU_N44 = 'N44'
    """Libra por pie día"""
    CU_N45 = 'N45'
    """Metro cúbico por segundo pascal"""
    CU_N46 = 'N46'
    """Pie poundal"""
    CU_N47 = 'N47'
    """Pulgada poundal"""
    CU_N48 = 'N48'
    """Watt por centímetro cuadrado"""
    CU_N49 = 'N49'
    """Watt por pulgada cuadrada"""
    CU_N50 = 'N50'
    """Unidad térmica británica (tabla internacional) por pie cuadrado hora."""
    CU_N51 = 'N51'
    """Unidad térmica británica (termoquímica) por pie cuadrado hora."""
    CU_N52 = 'N52'
    """Unidad térmica británica (termoquímico) por pie cuadrado minuto."""
    CU_N53 = 'N53'
    """Unidad térmica británica (tabla internacional) por pie cuadrado segundo."""
    CU_N54 = 'N54'
    """Unidad térmica británica (termoquímica) por pie cuadrado segundo."""
    CU_N55 = 'N55'
    """Unidad térmica británica (tabla internacional) por pulgada cuadrada segundo."""
    CU_N56 = 'N56'
    """Caloría (termoquímica) por centímetro cuadrado minuto"""
    CU_N57 = 'N57'
    """Caloría (termoquímica) por centímetro cuadrado segundo"""
    CU_N58 = 'N58'
    """Unidad térmica británica (tabla internacional) por pie cúbico"""
    CU_N59 = 'N59'
    """Unidad térmica británica (termoquímica) por pie cúbico"""
    CU_N60 = 'N60'
    """Unidad térmica británica (tabla internacional) por grado fahrenheit"""
    CU_N61 = 'N61'
    """Unidad térmica británica (termoquímico) por grado fahrenheit"""
    CU_N62 = 'N62'
    """Unidad térmica británica (tabla internacional) por grado rankine"""
    CU_N63 = 'N63'
    """Unidad térmica británica (termoquímico) por grado rankine"""
    CU_N64 = 'N64'
    """Unidad térmica británica (termoquímico) por libra grado rankine"""
    CU_N65 = 'N65'
    """Kilocaloría (tabla internacional) por gramo kelvin"""
    CU_N66 = 'N66'
    """Unidad térmica británica (39 °f)"""
    CU_N67 = 'N67'
    """Unidad térmica británica (59 °f)"""
    CU_N68 = 'N68'
    """Unidad térmica británica (60 °f)"""
    CU_N69 = 'N69'
    """Caloría (20 °c)"""
    CU_N70 = 'N70'
    """Quad"""
    CU_N71 = 'N71'
    """Termia (energía comercial)"""
    CU_N72 = 'N72'
    """Termia (UEA)"""
    CU_N73 = 'N73'
    """Unidad térmica británica (termoquímica) por libra"""
    CU_N74 = 'N74'
    """Unidad térmica británica (tabla internacional) por hora pie cuadrado grado fahrenheit."""
    CU_N75 = 'N75'
    """Unidad térmica británica (termoquímico) por hora pie cuadrado grado farenheit."""
    CU_N76 = 'N76'
    """Unidad térmica británica (tabla internacional) por segundo pie cuadrado grado fahrenheit."""
    CU_N77 = 'N77'
    """Unidad térmica británica (termoquímico) por segundo pie cuadrado grado fahrenheit."""
    CU_N78 = 'N78'
    """Kilowatt por metro cuadrado kelvin"""
    CU_N79 = 'N79'
    """Kelvin por pascal"""
    CU_N80 = 'N80'
    """Watt por metro grado celsius"""
    CU_N81 = 'N81'
    """Kilowatt por metro kelvin"""
    CU_N82 = 'N82'
    """Kilowatt por metro grado celsius"""
    CU_N83 = 'N83'
    """Metro por grado celsius metro"""
    CU_N84 = 'N84'
    """Grado fahrenheit hora por unidad térmica británica (tabla internacional)"""
    CU_N85 = 'N85'
    """Grado fahrenheit hora por unidad térmica británica (termoquímico)"""
    CU_N86 = 'N86'
    """Grado fahrenheit segundo por unidad térmica británica (tabla internacional)"""
    CU_N87 = 'N87'
    """Grago fahrenheit segundo por unidad térmica británica (termoquímico)"""
    CU_N88 = 'N88'
    """Grado fahrenheit hora pie cuadrado por unidad térmica británica (tabla internacional) pulgada"""
    CU_N89 = 'N89'
    """Grado fahrenheit hora pie cuadrado por unidad térmica británica (termoquímico) pulgada."""
    CU_N90 = 'N90'
    """Kilofaradio"""
    CU_N91 = 'N91'
    """Joule recíproco"""
    CU_N92 = 'N92'
    """Picosiemens"""
    CU_N93 = 'N93'
    """Amperio por pascal"""
    CU_N94 = 'N94'
    """Franklin"""
    CU_N95 = 'N95'
    """Amperio minuto"""
    CU_N96 = 'N96'
    """Biot"""
    CU_N97 = 'N97'
    """Gilbert"""
    CU_N98 = 'N98'
    """Voltio por pascal"""
    CU_N99 = 'N99'
    """Picovoltio"""
    CU_NA = 'NA'
    """Miligramo por kilogramo"""
    CU_NAR = 'NAR'
    """Número de artículos"""
    CU_NB = 'NB'
    """barcaza"""
    CU_NBB = 'NBB'
    """Número de bobinas"""
    CU_NC = 'NC'
    """Carro"""
    CU_NCL = 'NCL'
    """Número de células"""
    CU_ND = 'ND'
    """Barril neto"""
    CU_NE = 'NE'
    """Litro neto"""
    CU_NEW = 'NEW'
    """Newton"""
    CU_NF = 'NF'
    """Mensaje"""
    CU_NG = 'NG'
    """Galón neto (us)"""
    CU_NH = 'NH'
    """Hora del mensaje"""
    CU_NI = 'NI'
    """Galón imperial neto"""
    CU_NIL = 'NIL'
    """Nil"""
    CU_NIU = 'NIU'
    """Número de unidades internacionales"""
    CU_NJ = 'NJ'
    """Número de pantallas"""
    CU_NL = 'NL'
    """Carga"""
    CU_NM3 = 'NM3'
    """Metro cúbico normalizado"""
    CU_NMI = 'NMI'
    """Milla náutica"""
    CU_NMP = 'NMP'
    """Número de paquetes"""
    CU_NN = 'NN'
    """tren"""
    CU_NPR = 'NPR'
    """Número de parejas"""
    CU_NPT = 'NPT'
    """Número de partes"""
    CU_NQ = 'NQ'
    """Mho"""
    CU_NR = 'NR'
    """Micromho"""
    CU_NT = 'NT'
    """Tonelada neta"""
    CU_NTT = 'NTT'
    """Tonelada de registro neto"""
    CU_NV = 'NV'
    """vehículo"""
    CU_NY = 'NY'
    """Libra por tonelada métrica al aire seco"""
    CU_NX = 'NX'
    """Parte por mil"""
    CU_OA = 'OA'
    """Panel"""
    CU_ODE = 'ODE'
    """Equivalente de agotamiento del ozona"""
    CU_Ohm = 'Ohm'
    """Ohm"""
    CU_ON = 'ON'
    """Onza por yarda cuadrada"""
    CU_ONZ = 'ONZ'
    """Onza (avoirdupois)"""
    CU_OP = 'OP'
    """Dos paquetes"""
    CU_OPM = 'OPM'
    """Oscilaciones por minuto"""
    CU_OT = 'OT'
    """Hora extra"""
    CU_OZ = 'OZ'
    """Onza AV"""
    CU_OZA = 'OZA'
    """Onza líquida (estados unidos)"""
    CU_OZI = 'OZI'
    """Onza líquida (UK)"""
    CU_P0 = 'P0'
    """Página electrónica"""
    CU_P1 = 'P1'
    """Tanto por ciento"""
    CU_P10 = 'P10'
    """Culombio por metro"""
    CU_P11 = 'P11'
    """Kiloweber"""
    CU_P12 = 'P12'
    """Gamma"""
    CU_P13 = 'P13'
    """Kilotesla"""
    CU_P14 = 'P14'
    """Joule por segundo"""
    CU_P15 = 'P15'
    """Joule por minuto"""
    CU_P16 = 'P16'
    """Joule por hora"""
    CU_P17 = 'P17'
    """Joule por día"""
    CU_P18 = 'P18'
    """Kilojoule por segundo"""
    CU_P19 = 'P19'
    """Kilojoule por minuto"""
    CU_P2 = 'P2'
    """Libra por pie"""
    CU_P20 = 'P20'
    """Kilojoule por hora"""
    CU_P21 = 'P21'
    """Kilojoule por día"""
    CU_P22 = 'P22'
    """NanoOhm"""
    CU_P23 = 'P23'
    """Ohm circular-mil por pie"""
    CU_P24 = 'P24'
    """Kilohenry"""
    CU_P25 = 'P25'
    """Lumen por pie cuadrado"""
    CU_P26 = 'P26'
    """Foto"""
    CU_P27 = 'P27'
    """Vela (medida)"""
    CU_P28 = 'P28'
    """Candela por pulgada cuadrada"""
    CU_P29 = 'P29'
    """Footlambert"""
    CU_P3 = 'P3'
    """Tres paquetes"""
    CU_P30 = 'P30'
    """Lambert"""
    CU_P31 = 'P31'
    """Stilb"""
    CU_P32 = 'P32'
    """Candela por pie cuadrado"""
    CU_P33 = 'P33'
    """Kilocandela"""
    CU_P34 = 'P34'
    """Milicandela"""
    CU_P35 = 'P35'
    """Hefner-kerze"""
    CU_P36 = 'P36'
    """Candela internacional"""
    CU_P37 = 'P37'
    """Unidad térmica británica (tabla internacional) por pie cuadrado"""
    CU_P38 = 'P38'
    """Unidad térmica británica (termoquímica) por pie cuadrado"""
    CU_P39 = 'P39'
    """Caloría (termoquímica) por centímetro cuadrado"""
    CU_P4 = 'P4'
    """paquete de cuatro"""
    CU_P40 = 'P40'
    """Langley"""
    CU_P41 = 'P41'
    """Década (logarítmica)"""
    CU_P42 = 'P42'
    """Pascal por segundo cuadrado"""
    CU_P43 = 'P43'
    """Bel por metro"""
    CU_P44 = 'P44'
    """Libra Mol"""
    CU_P45 = 'P45'
    """Libra de Mol por segundo"""
    CU_P46 = 'P46'
    """Libra Mol por minuto"""
    CU_P47 = 'P47'
    """KiloMol por kilogramo"""
    CU_P48 = 'P48'
    """Libra de Mol por libra"""
    CU_P49 = 'P49'
    """Newton metro cuadrado por amperio"""
    CU_P5 = 'P5'
    """Paquete de cinco"""
    CU_P50 = 'P50'
    """Metro weber"""
    CU_P51 = 'P51'
    """Mol por kilogramo pascal"""
    CU_P52 = 'P52'
    """Mol por metro cúbico pascal"""
    CU_P53 = 'P53'
    """Unit por segundo"""
    CU_P54 = 'P54'
    """MiliGray por segundo"""
    CU_P55 = 'P55'
    """MicroGray por segundo"""
    CU_P56 = 'P56'
    """NanoGray por segundo"""
    CU_P57 = 'P57'
    """Gray por minuto"""
    CU_P58 = 'P58'
    """MiliGray por minuto"""
    CU_P59 = 'P59'
    """Microgray por minuto"""
    CU_P6 = 'P6'
    """paquete de seis"""
    CU_P60 = 'P60'
    """Nanogray por minuto"""
    CU_P61 = 'P61'
    """Gray por hora"""
    CU_P62 = 'P62'
    """MiliGray por hora"""
    CU_P63 = 'P63'
    """Micro gray por hora"""
    CU_P64 = 'P64'
    """Nanogray por hora"""
    CU_P65 = 'P65'
    """Sievert por segundo"""
    CU_P66 = 'P66'
    """MilliSievert por segundo"""
    CU_P67 = 'P67'
    """MicroSievert por segundo"""
    CU_P68 = 'P68'
    """NanoSievert por segundo"""
    CU_P69 = 'P69'
    """Rem por segundo"""
    CU_P7 = 'P7'
    """Paquete de siete"""
    CU_P70 = 'P70'
    """Sievert por hora"""
    CU_P71 = 'P71'
    """MilliSievert por hora"""
    CU_P72 = 'P72'
    """Micro Sievert por hora"""
    CU_P73 = 'P73'
    """NanoSievert por hora"""
    CU_P74 = 'P74'
    """Sievert por minuto"""
    CU_P75 = 'P75'
    """MilliSievert por minuto"""
    CU_P76 = 'P76'
    """MicroSievert por minuto"""
    CU_P77 = 'P77'
    """NanoSievert pominut"""
    CU_P78 = 'P78'
    """Reciprocidad por segundo"""
    CU_P79 = 'P79'
    """Pascal metro cuadrado por kilogramo"""
    CU_P8 = 'P8'
    """Paquete de ocho"""
    CU_P80 = 'P80'
    """Milipascal por metro."""
    CU_P81 = 'P81'
    """Kilopascal por metro."""
    CU_P82 = 'P82'
    """Hectopascal por metro."""
    CU_P83 = 'P83'
    """Atmosfera estándar por metro."""
    CU_P84 = 'P84'
    """Atmosfera técnica por metro."""
    CU_P85 = 'P85'
    """Torr por metro."""
    CU_P86 = 'P86'
    """Psi por pulgada"""
    CU_P87 = 'P87'
    """Metro cúbico por segundo de metro cuadrado"""
    CU_P88 = 'P88'
    """Rhe"""
    CU_P89 = 'P89'
    """Libra por metro cúbico de pulgada"""
    CU_P9 = 'P9'
    """Nueve paquetes"""
    CU_P90 = 'P90'
    """Libra-fuerza por pulgada cuadrada"""
    CU_P91 = 'P91'
    """Permanente (0°c)"""
    CU_P92 = 'P92'
    """Permanente (23°c)"""
    CU_P93 = 'P93'
    """Byte por segundo"""
    CU_P94 = 'P94'
    """Kilobyte por segundo"""
    CU_P95 = 'P95'
    """Megabite por segundo"""
    CU_P96 = 'P96'
    """Recíproco de la unidad si deriva voltio"""
    CU_P97 = 'P97'
    """Reciprocidad de Radian"""
    CU_P98 = 'P98'
    """Pascal a la suma de potencia de los números estequimetricos"""
    CU_P99 = 'P99'
    """Mols por metro cúbico a la suma de potencia de los números estequimetricos"""
    CU_PAL = 'PAL'
    """Pascal"""
    CU_PB = 'PB'
    """Par de la pulgada"""
    CU_PD = 'PD'
    """Almohadilla"""
    CU_PE = 'PE'
    """Libra equivalente"""
    CU_PFL = 'PFL'
    """Litro de prueba"""
    CU_PGL = 'PGL'
    """Galón de prueba"""
    CU_PI = 'PI'
    """Tono"""
    CU_PLA = 'PLA'
    """Grado de platón"""
    CU_PM = 'PM'
    """Porcentaje de libra"""
    CU_PO = 'PO'
    """Libra por pulgada"""
    CU_PQ = 'PQ'
    """Página por pulgada"""
    CU_PR = 'PR'
    """Par"""
    CU_PS = 'PS'
    """Libra fuerza por pulgada cuadrada"""
    CU_PT = 'PT'
    """Pinta (US)"""
    CU_PTD = 'PTD'
    """Pinta seca (estados unidos)"""
    CU_PTI = 'PTI'
    """Pint (uk)"""
    CU_PTL = 'PTL'
    """Pinta líquida (estados unidos)"""
    CU_PTN = 'PTN'
    """Parte"""
    CU_PV = 'PV'
    """Media pinta (US)"""
    CU_PW = 'PW'
    """Libra por pulgada de ancho"""
    CU_PY = 'PY'
    """Pico seco (EUA)"""
    CU_PZ = 'PZ'
    """Peck dry (UK)"""
    CU_Q10 = 'Q10'
    """Joule por tesla"""
    CU_Q11 = 'Q11'
    """Erlang"""
    CU_Q12 = 'Q12'
    """Octeto"""
    CU_Q13 = 'Q13'
    """Octeto por segundo"""
    CU_Q14 = 'Q14'
    """Shannon"""
    CU_Q15 = 'Q15'
    """Hartley"""
    CU_Q16 = 'Q16'
    """Unidad natural de información"""
    CU_Q17 = 'Q17'
    """Shannon por segundo"""
    CU_Q18 = 'Q18'
    """Hartley por segundo"""
    CU_Q19 = 'Q19'
    """Unidad natural de información por segundo"""
    CU_Q20 = 'Q20'
    """Segundo por kilogramo"""
    CU_Q21 = 'Q21'
    """Watt metro cuadrado"""
    CU_Q22 = 'Q22'
    """Segundo por metro cúbicos de radianes"""
    CU_Q23 = 'Q23'
    """Weber a la potencia menos uno"""
    CU_Q24 = 'Q24'
    """Reciprocidad de Pulgada"""
    CU_Q25 = 'Q25'
    """Dioptría"""
    CU_Q26 = 'Q26'
    """Uno por uno"""
    CU_Q27 = 'Q27'
    """Newtons metros por metro"""
    CU_Q28 = 'Q28'
    """Kilogramo por metro cuadrado pascal segundo"""
    CU_Q29 = 'Q29'
    """Microgramo por hectogramo"""
    CU_Q3 = 'Q3'
    """Comida"""
    CU_Q30 = 'Q30'
    """Ph (potencial de hidrogeno)"""
    CU_Q31 = 'Q31'
    """Kilojoule por gramo"""
    CU_Q32 = 'Q32'
    """Femtolitro"""
    CU_Q33 = 'Q33'
    """Picolitro"""
    CU_Q34 = 'Q34'
    """Nanolitro"""
    CU_Q35 = 'Q35'
    """Megawatts por minuto"""
    CU_Q36 = 'Q36'
    """Metro cuadrado por metro cúbico"""
    CU_Q37 = 'Q37'
    """Metro cúbico estándar por día"""
    CU_Q38 = 'Q38'
    """Metro cúbico estándar por hora"""
    CU_Q39 = 'Q39'
    """Metro cúbico normalizado por día"""
    CU_Q40 = 'Q40'
    """Metro cúbico normalizado por hora"""
    CU_Q41 = 'Q41'
    """Joule por metro cúbico normalizado"""
    CU_Q42 = 'Q42'
    """Joule por metro cúbico estándar"""
    CU_QA = 'QA'
    """Página-fascimil"""
    CU_QAN = 'QAN'
    """Cuarto (de un año)"""
    CU_QB = 'QB'
    """Página, copia impresa"""
    CU_QD = 'QD'
    """Cuarta docena"""
    CU_QH = 'QH'
    """Un cuarto de hora"""
    CU_QK = 'QK'
    """Cuarto de kilogramo"""
    CU_QR = 'QR'
    """Mano de papel"""
    CU_QT = 'QT'
    """Cuarto (EUA)"""
    CU_QTD = 'QTD'
    """Cuarto seco (estados unidos)"""
    CU_QTI = 'QTI'
    """Cuarto (UK)"""
    CU_QTL = 'QTL'
    """Cuarto de líquido (estados unidos)"""
    CU_QTR = 'QTR'
    """Cuarto"""
    CU_R1 = 'R1'
    """Pica"""
    CU_R9 = 'R9'
    """Mil metros cúbicos"""
    CU_RH = 'RH'
    """Hora de funcionamiento"""
    CU_RK = 'RK'
    """Medida métrica de rollo"""
    CU_RM = 'RM'
    """Resma"""
    CU_RN = 'RN'
    """Medida métrica de Hojas (resma)"""
    CU_ROM = 'ROM'
    """Habitación"""
    CU_RP = 'RP'
    """Libra por resma"""
    CU_RPM = 'RPM'
    """Revoluciones por minuto"""
    CU_RPS = 'RPS'
    """Revoluciones por segundo"""
    CU_RS = 'RS'
    """Reiniciar"""
    CU_RT = 'RT'
    """Milla de toneladas de ingresos"""
    CU_RU = 'RU'
    """correr"""
    CU_S3 = 'S3'
    """Pie cuadrado por segundo"""
    CU_S4 = 'S4'
    """Metro cuadrado por segundo"""
    CU_S5 = 'S5'
    """Sesenta cuartos de pulgada"""
    CU_S6 = 'S6'
    """Sesión"""
    CU_S7 = 'S7'
    """unidad de almacenamiento"""
    CU_S8 = 'S8'
    """Unidad de publicidad estándar"""
    CU_SAN = 'SAN'
    """Medio año"""
    CU_SCO = 'SCO'
    """Puntuación"""
    CU_SCR = 'SCR'
    """Escrúpulo"""
    CU_SD = 'SD'
    """Libra sólida"""
    CU_SE = 'SE'
    """Sección"""
    CU_SEC = 'SEC'
    """Segundo [unidad de tiempo]"""
    CU_SET = 'SET'
    """Conjunto"""
    CU_SG = 'SG'
    """Segmento"""
    CU_SHT = 'SHT'
    """Tonelada de envíos"""
    CU_SIE = 'SIE'
    """Siemens"""
    CU_SK = 'SK'
    """Camión cisterna con división"""
    CU_SM3 = 'SM3'
    """Metro cúbico estándar"""
    CU_SMI = 'SMI'
    """Milla (milla estatal)"""
    CU_SN = 'SN'
    """Barra cuadrada"""
    CU_SQ = 'SQ'
    """Cuadrado"""
    CU_SQR = 'SQR'
    """Cuadrado y techado"""
    CU_SR = 'SR'
    """Tira"""
    CU_SS = 'SS'
    """Medida métrica de hoja"""
    CU_SST = 'SST'
    """Estándar corto (7200 partidos)"""
    CU_STC = 'STC'
    """Palo"""
    CU_STI = 'STI'
    """Estone (UK)"""
    CU_STK = 'STK'
    """Palo, cigarrillo"""
    CU_STL = 'STL'
    """Litro estándar"""
    CU_STN = 'STN'
    """Tonelada (estados unidos) o tonelada corta (UK y estados unidos)"""
    CU_STW = 'STW'
    """Paja"""
    CU_SW = 'SW'
    """Número de madejas"""
    CU_SX = 'SX'
    """Envío"""
    CU_SYR = 'SYR'
    """Jeringuilla"""
    CU_T0 = 'T0'
    """Línea de telecomunicaciones en servicio"""
    CU_T1 = 'T1'
    """Mil libras"""
    CU_T3 = 'T3'
    """Mil pedazos"""
    CU_T4 = 'T4'
    """Bolsa de mil"""
    CU_T5 = 'T5'
    """Mil envolturas"""
    CU_T6 = 'T6'
    """Mil galones (US)"""
    CU_T7 = 'T7'
    """Impresión de mil"""
    CU_T8 = 'T8'
    """Mil pulgadas lineales"""
    CU_TA = 'TA'
    """Décimo de pie cúbico"""
    CU_TAB = 'TAB'
    """Tonelada de registro bruto"""
    CU_TAH = 'TAH'
    """Kiloamperio-hora (milamperio-hora)"""
    CU_TAN = 'TAN'
    """Número de acido total"""
    CU_TC = 'TC'
    """Camión"""
    CU_TD = 'TD'
    """Térmico"""
    CU_TE = 'TE'
    """Totalizador"""
    CU_TF = 'TF'
    """Diez yardas cuadradas"""
    CU_TI = 'TI'
    """Mil pulgadas cuadradas"""
    CU_TIC = 'TIC'
    """Tonelada métrica, incluido el contenedor"""
    CU_TIP = 'TIP'
    """Tonelada métrica, incluido el embalaje interior"""
    CU_TJ = 'TJ'
    """Mil centímetros cuadrados"""
    CU_TKM = 'TKM'
    """Tonelada kilometro"""
    CU_TL = 'TL'
    """Mil pies (lineal)"""
    CU_TMS = 'TMS'
    """Kilogramo de carne importada, menos despojos"""
    CU_TNE = 'TNE'
    """Tonelada (tonelada métrica)"""
    CU_TP = 'TP'
    """Paquete de diez"""
    CU_TPI = 'TPI'
    """Dientes por pulgada"""
    CU_TPR = 'TPR'
    """Decenas de pares"""
    CU_TQ = 'TQ'
    """Mil pies"""
    CU_TQD = 'TQD'
    """Mil metros cúbicos por día"""
    CU_TR = 'TR'
    """Diez pies cuadrados"""
    CU_TRL = 'TRL'
    """Trillones (eur)"""
    CU_Ts = 'Ts'
    """Mil pies cuadrados"""
    CU_TSD = 'TSD'
    """Tonelada de sustancia 90% seca"""
    CU_TSH = 'TSH'
    """Tonelada de vapor por hora"""
    CU_TST = 'TST'
    """Decena de conjuntos"""
    CU_TT = 'TT'
    """Mil metros lineales"""
    CU_TTS = 'TTS'
    """Decenas de millar de pegatinas"""
    CU_Tu = 'Tu'
    """Contenedor externo"""
    CU_TV = 'TV'
    """Mil kilogramos"""
    CU_TW = 'TW'
    """Mil hojas"""
    CU_U1 = 'U1'
    """Tratamiento"""
    CU_U2 = 'U2'
    """Número de tabletas"""
    CU_UA = 'UA'
    """Torr"""
    CU_UB = 'UB'
    """Línea de telecomunicaciones en servicio promedio"""
    CU_UC = 'UC'
    """Puerto de telecomunicaciones"""
    CU_UD = 'UD'
    """Décimo minuto"""
    CU_UE = 'UE'
    """Hora de décimo"""
    CU_UF = 'UF'
    """Uso por línea de telecomunicaciones promedio"""
    CU_UH = 'UH'
    """Diez mil yardas"""
    CU_UM = 'UM'
    """Millón de unidades"""
    CU_UN = 'UN'
    """Newton metro"""
    CU_VA = 'VA'
    """Voltio-amperio por kilogramo"""
    CU_VLT = 'VLT'
    """Voltio"""
    CU_VP = 'VP'
    """Volumen porcentual"""
    CU_VS = 'VS'
    """Visita"""
    CU_W2 = 'W2'
    """Kilo húmedo"""
    CU_W4 = 'W4'
    """Dos semanas"""
    CU_WA = 'WA'
    """Watt por kilogramo"""
    CU_WB = 'WB'
    """Libra húmeda"""
    CU_WCD = 'WCD'
    """Cable"""
    CU_WE = 'WE'
    """Tonelada húmeda"""
    CU_WEB = 'WEB'
    """Weber"""
    CU_WEE = 'WEE'
    """Semana"""
    CU_WG = 'WG'
    """Galón de vino"""
    CU_WH = 'WH'
    """Rueda"""
    CU_WHR = 'WHR'
    """Watt hora"""
    CU_WI = 'WI'
    """Peso por pulgada cuadrada"""
    CU_WM = 'WM'
    """Mes de trabajo"""
    CU_WR = 'WR'
    """Envolver"""
    CU_WSD = 'WSD'
    """Estándar"""
    CU_WTT = 'WTT'
    """Watt"""
    CU_WW = 'WW'
    """Mililitro de agua"""
    CU_X1 = 'X1'
    """Cadena de gunter"""
    CU_X1A = 'X1A'
    """Tambor de acero"""
    CU_X1B = 'X1B'
    """Tambor de aluminio"""
    CU_X1D = 'X1D'
    """Tambor contrachapado"""
    CU_X1F = 'X1F'
    """Contenedor flexible"""
    CU_X1G = 'X1G'
    """Tambor de fibra"""
    CU_X1w = 'X1w'
    """Tambor de madera"""
    CU_X2C = 'X2C'
    """Barril de madera"""
    CU_X3A = 'X3A'
    """Bidón de acero"""
    CU_X3H = 'X3H'
    """Bidón de plástico"""
    CU_X43 = 'X43'
    """Bolsa de gran tamaño"""
    CU_X44 = 'X44'
    """Bolsa de plástico"""
    CU_X4A = 'X4A'
    """Caja de acero"""
    CU_X4B = 'X4B'
    """Caja de aluminio"""
    CU_X4C = 'X4C'
    """Caja de  madera natural"""
    CU_X4D = 'X4D'
    """Caja de contrachapado"""
    CU_X4F = 'X4F'
    """Caja de madera reconstituida"""
    CU_X4G = 'X4G'
    """Caja de cartón"""
    CU_X4H = 'X4H'
    """Caja de plástico"""
    CU_X5H = 'X5H'
    """Bolsa de plástico tejido"""
    CU_X5L = 'X5L'
    """Bolsa textil"""
    CU_X5M = 'X5M'
    """Bolsa de papel"""
    CU_X6H = 'X6H'
    """Recipiente de plástico, Contenedor compuesto."""
    CU_X6P = 'X6P'
    """Recipiente de vidrio, Contenedor compuesto."""
    CU_X7A = 'X7A'
    """Estuche para carro"""
    CU_X7B = 'X7B'
    """Estuche de madera"""
    CU_X8A = 'X8A'
    """Pallet de madera"""
    CU_X8B = 'X8B'
    """Cajón de madera"""
    CU_X8C = 'X8C'
    """Madera flejada"""
    CU_XAA = 'XAA'
    """Contenedor intermedio  para gráneles de plástico rígido"""
    CU_XAB = 'XAB'
    """Contenedor de fibra"""
    CU_XAC = 'XAC'
    """Contenedor de papel"""
    CU_XAD = 'XAD'
    """Contenedor de madera"""
    CU_XAE = 'XAE'
    """Aerosol"""
    CU_XAF = 'XAF'
    """Pallet modular con collares,  80cms * 60cms"""
    CU_XAG = 'XAG'
    """Pallet o empaquetado"""
    CU_XAH = 'XAH'
    """Pallet, 100cms X 110cms"""
    CU_XAI = 'XAI'
    """Contenedor tipo concha"""
    CU_XAJ = 'XAJ'
    """Cono"""
    CU_XAL = 'XAL'
    """Esfera"""
    CU_XAM = 'XAM'
    """Ampolleta no protegida"""
    CU_XAP = 'XAP'
    """Ampolleta protegida"""
    CU_XAT = 'XAT'
    """Atomizador"""
    CU_XAV = 'XAV'
    """Cápsula"""
    CU_XB4 = 'XB4'
    """Cinturón"""
    CU_XBA = 'XBA'
    """Barril"""
    CU_XBB = 'XBB'
    """Bobina"""
    CU_XBC = 'XBC'
    """Cajón para botellas / Estante para botellas"""
    CU_XBD = 'XBD'
    """Tablero"""
    CU_XBE = 'XBE'
    """Flejado"""
    CU_XBF = 'XBF'
    """Globo no protegido"""
    CU_XBG = 'XBG'
    """Bolso"""
    CU_XBH = 'XBH'
    """Manojo"""
    CU_XBI = 'XBI'
    """Compartimiento"""
    CU_XBJ = 'XBJ'
    """Cubeta"""
    CU_XBK = 'XBK'
    """Cesta"""
    CU_XBL = 'XBL'
    """Paca comprimida"""
    CU_XBM = 'XBM'
    """Cuenco"""
    CU_XBN = 'XBN'
    """Paca no comprimida"""
    CU_XBO = 'XBO'
    """Botella no-protegida y cilíndrica"""
    CU_XBP = 'XBP'
    """Globo protegido"""
    CU_XBQ = 'XBQ'
    """Botella cilíndrica protegida"""
    CU_XBR = 'XBR'
    """Barra"""
    CU_XBS = 'XBS'
    """Botella, no-protegida en forma de bulbo"""
    CU_XBT = 'XBT'
    """Rollo de tela"""
    CU_XBU = 'XBU'
    """Butt"""
    CU_XBV = 'XBV'
    """Botella de bulbo protegido"""
    CU_XBW = 'XBW'
    """Caja para líquidos"""
    CU_XBX = 'XBX'
    """Caja"""
    CU_XBY = 'XBY'
    """Tablero, con fleje/ agrupados/ armados"""
    CU_XBZ = 'XBZ'
    """Barras, con fleje/ agrupados/ armados"""
    CU_XCA = 'XCA'
    """Lata rectangular"""
    CU_XCB = 'XCB'
    """Cajón para cerveza"""
    CU_XCC = 'XCC'
    """Mantequera"""
    CU_XCD = 'XCD'
    """Lata con mango y boquilla"""
    CU_XCE = 'XCE'
    """Cesto tejido"""
    CU_XCF = 'XCF'
    """Cofre"""
    CU_XCG = 'XCG'
    """Contenedor tipo Jaula"""
    CU_XCH = 'XCH'
    """Cajonera"""
    CU_XCI = 'XCI'
    """Frasco"""
    CU_XCJ = 'XCJ'
    """Ataúd"""
    CU_XCK = 'XCK'
    """Barrica"""
    CU_XCL = 'XCL'
    """Espiral"""
    CU_XCM = 'XCM'
    """Paquete de tarjetas"""
    CU_XCN = 'XCN'
    """Contenedor, no especificado como equipo de transporte"""
    CU_XCO = 'XCO'
    """Garrafón no protegido"""
    CU_XCP = 'XCP'
    """Garrafón protegido"""
    CU_XCQ = 'XCQ'
    """Cartucho"""
    CU_XCR = 'XCR'
    """Cajón"""
    CU_XCS = 'XCS'
    """Estuche"""
    CU_XCT = 'XCT'
    """Cartón"""
    CU_XCU = 'XCU'
    """Vaso"""
    CU_XCV = 'XCV'
    """Cubierta"""
    CU_XCW = 'XCW'
    """Jaula estilo rodillo"""
    CU_XCX = 'XCX'
    """Lata cilíndrica"""
    CU_XCY = 'XCY'
    """Cilindro"""
    CU_XCZ = 'XCZ'
    """Lona"""
    CU_XDA = 'XDA'
    """Cajón multicapa de plástico"""
    CU_XDB = 'XDB'
    """Cajón de varias capas de madera"""
    CU_XDC = 'XDC'
    """Cajón multicapa de cartón"""
    CU_XDG = 'XDG'
    """Jaula, Según la clasificación de la compañía (Commonwealth Handling Equipment Pool (CHEP))"""
    CU_XDH = 'XDH'
    """Caja, Según la clasificación de la compañía (CHEP), Eurobox"""
    CU_XDI = 'XDI'
    """Tambor de hierro"""
    CU_XDJ = 'XDJ'
    """damajuana o garrafa, no protegido"""
    CU_XDK = 'XDK'
    """Cajón a granel, cartón"""
    CU_XDL = 'XDL'
    """Cajas de plástico"""
    CU_XDM = 'XDM'
    """Cajones a granel de madera"""
    CU_XDN = 'XDN'
    """Dispensador"""
    CU_XDP = 'XDP'
    """damajuana o garrafa, protegido"""
    CU_XDR = 'XDR'
    """Tambor"""
    CU_XDS = 'XDS'
    """Bandeja de una capa sin cubierta y de plástico"""
    CU_XDT = 'XDT'
    """Bandeja de una capa sin cubierta y de madera"""
    CU_XDU = 'XDU'
    """Bandeja de una capa sin cubierta y  poliestireno"""
    CU_XDV = 'XDV'
    """Bandeja de una capa sin cubierta y de cartón"""
    CU_XDW = 'XDW'
    """Bandeja de dos capas sin tapa y con bandeja de plástico"""
    CU_XDX = 'XDX'
    """Bandeja de dos capas sin cubierta y de madera"""
    CU_XDY = 'XDY'
    """Bandeja de dos capas sin cubierta y de cartón"""
    CU_XEC = 'XEC'
    """Bolsa de plástico"""
    CU_XED = 'XED'
    """Estuche, con pallet de base"""
    CU_XEE = 'XEE'
    """Estuche, con pallet base de madera"""
    CU_XEF = 'XEF'
    """Estuche, con pallet base de cartón"""
    CU_XEG = 'XEG'
    """Estuche, con pallet base de plástico"""
    CU_XEH = 'XEH'
    """Estuche, con pallet base de metal"""
    CU_XEI = 'XEI'
    """Estuche isotérmico"""
    CU_XEN = 'XEN'
    """Sobre"""
    CU_XFB = 'XFB'
    """Bolsa flexible"""
    CU_XFC = 'XFC'
    """Cajón para fruta"""
    CU_XFD = 'XFD'
    """Cajón enmarcado"""
    CU_XFE = 'XFE'
    """Tanque flexible"""
    CU_XFI = 'XFI'
    """Firkin"""
    CU_XFL = 'XFL'
    """Matraz"""
    CU_XFO = 'XFO'
    """Cajón para zapatos"""
    CU_XFP = 'XFP'
    """Caja auxiliar para película fotográfica"""
    CU_XFR = 'XFR'
    """Marco"""
    CU_XFT = 'XFT'
    """Contenedor para alimentos"""
    CU_XFW = 'XFW'
    """Carro de cama plana"""
    CU_XFX = 'XFX'
    """Bolsa flexible tipo contenedor"""
    CU_XGB = 'XGB'
    """Botella para gas"""
    CU_XGI = 'XGI'
    """Viga"""
    CU_XGL = 'XGL'
    """Contenedor tipo galón"""
    CU_XGR = 'XGR'
    """Recipiente de vidrio"""
    CU_XGU = 'XGU'
    """Bandeja contenedor para apilar horizontalmente objetos planos"""
    CU_XGY = 'XGY'
    """Costal de Yute"""
    CU_XGZ = 'XGZ'
    """Vigas con correas o agrupadas"""
    CU_XHA = 'XHA'
    """Cesta con mango y de plástico"""
    CU_XHB = 'XHB'
    """Cesta con mango y de madera"""
    CU_XHC = 'XHC'
    """Cesta  con asa y de  cartón"""
    CU_XHG = 'XHG'
    """Hogshead"""
    CU_XHN = 'XHN'
    """Gancho"""
    CU_XHR = 'XHR'
    """Cesto"""
    CU_XIA = 'XIA'
    """Paquete con pantalla y de madera"""
    CU_XIB = 'XIB'
    """Paquete  con pantalla y de cartón"""
    CU_XIC = 'XIC'
    """Paquete con pantalla y de plástico"""
    CU_XID = 'XID'
    """Paquete con pantalla y de metal"""
    CU_XIE = 'XIE'
    """Paquete de mostrador."""
    CU_XIF = 'XIF'
    """Envase para alimentos"""
    CU_XIG = 'XIG'
    """Paquete envuelto en papel"""
    CU_XIH = 'XIH'
    """Tambor de plástico"""
    CU_XIK = 'XIK'
    """Paquete de cartón con los agujeros para botellas"""
    CU_XIL = 'XIL'
    """Bandeja rígida con tapa y apilable (CEN TS 14482: 2002)"""
    CU_XIN = 'XIN'
    """Lingote"""
    CU_XIZ = 'XIZ'
    """Lingotes  con correas/ agrupados"""
    CU_XJB = 'XJB'
    """Bolsa jumbo"""
    CU_XJC = 'XJC'
    """Bidón rectangular"""
    CU_XJG = 'XJG'
    """Jarra"""
    CU_XJR = 'XJR'
    """Tarro"""
    CU_XJT = 'XJT'
    """Bolsa de yute"""
    CU_XJY = 'XJY'
    """Bidón, cilíndrico"""
    CU_XKG = 'XKG'
    """Barrilete"""
    CU_XKI = 'XKI'
    """Kit (Conjunto de piezas)"""
    CU_XLE = 'XLE'
    """Valijas"""
    CU_XLG = 'XLG'
    """Bitácora"""
    CU_XLT = 'XLT'
    """Lote"""
    CU_XLU = 'XLU'
    """Caja de arrastre"""
    CU_XLV = 'XLV'
    """Contenedor pequeño"""
    CU_XLZ = 'XLZ'
    """Registros  con fleje/ agrupados/ armados"""
    CU_XMA = 'XMA'
    """Cajón metálico"""
    CU_XMB = 'XMB'
    """Múltiplo de bolsas"""
    CU_XMC = 'XMC'
    """Cajón para leche"""
    CU_XME = 'XME'
    """Contenedor de metal"""
    CU_XMR = 'XMR'
    """Recipiente de metal"""
    CU_XMS = 'XMS'
    """Saco milti-pared"""
    CU_XMT = 'XMT'
    """Tapete"""
    CU_XMW = 'XMW'
    """Contenedor envuelto en plástico"""
    CU_XMX = 'XMX'
    """Caja pequeña de cerillos"""
    CU_XNA = 'XNA'
    """No disponible"""
    CU_XNE = 'XNE'
    """Sin empaque o no empaquetado"""
    CU_XNF = 'XNF'
    """Sin empaque o no empaquetado, unidad simple"""
    CU_XNG = 'XNG'
    """Sin empaque o no empaquetado, unidades múltiples"""
    CU_XNS = 'XNS'
    """Caja nido"""
    CU_XNT = 'XNT'
    """Red"""
    CU_XNU = 'XNU'
    """Red de plástico con tubo"""
    CU_XNV = 'XNV'
    """Red textil con tubo"""
    CU_XOA = 'XOA'
    """Pallet, Según la clasificación de la compañía (Commonwealth Handling Equipment Pool (CHEP) 40 cm x 60 cm"""
    CU_XOB = 'XOB'
    """Pallet, Según la clasificación de la compañía (Commonwealth Handling Equipment Pool (CHEP) 80 cm x 120 cm"""
    CU_XOC = 'XOC'
    """Pallet, Según la clasificación de la compañía (Commonwealth Handling Equipment Pool (CHEP) 100 cm x 120 cm"""
    CU_XOD = 'XOD'
    """Pallet, AS 4068-1993"""
    CU_XOE = 'XOE'
    """Pallet, ISO T11"""
    CU_XOF = 'XOF'
    """Plataforma, peso o dimensión no especificada"""
    CU_XOK = 'XOK'
    """Bloque"""
    CU_XOT = 'XOT'
    """Octabin"""
    CU_XP2 = 'XP2'
    """Charola"""
    CU_XPA = 'XPA'
    """Cajetilla"""
    CU_XPB = 'XPB'
    """Pallet, Caja combinada y abierta con caja y pallet."""
    CU_XPC = 'XPC'
    """Paquete postal"""
    CU_XPD = 'XPD'
    """Pallet modular con collares (80cms * 100cms)"""
    CU_XPE = 'XPE'
    """Pallet modular con collares (80cms * 120cms)"""
    CU_XPF = 'XPF'
    """Corral"""
    CU_XPG = 'XPG'
    """Placa"""
    CU_XPH = 'XPH'
    """Cantaro"""
    CU_XPI = 'XPI'
    """Pleca"""
    CU_XPJ = 'XPJ'
    """Canastilla"""
    CU_XPK = 'XPK'
    """Paquete"""
    CU_XPL = 'XPL'
    """Balde"""
    CU_XPN = 'XPN'
    """Tablón"""
    CU_XPO = 'XPO'
    """Bolsa pequeña"""
    CU_XPR = 'XPR'
    """Contenedor de plástico"""
    CU_XPT = 'XPT'
    """Maceta"""
    CU_XPU = 'XPU'
    """Cacerola"""
    CU_XPV = 'XPV'
    """Tubos, con fleje/ agrupados/ armados"""
    CU_XPX = 'XPX'
    """Pallet"""
    CU_XPY = 'XPY'
    """Placas con fleje/ agrupados/ armados"""
    CU_XPZ = 'XPZ'
    """Tablones con fleje/ agrupados/ armados"""
    CU_XQA = 'XQA'
    """Tambor de acero con cabeza no desmontable"""
    CU_XQB = 'XQB'
    """Tambor de  acero con cabeza extraíble"""
    CU_XQC = 'XQC'
    """Tambor de aluminio con cabeza no extraíble"""
    CU_XQD = 'XQD'
    """Tambor de aluminio con cabeza extraíble"""
    CU_XQF = 'XQF'
    """Tambor, plástico con cabeza no desmontable"""
    CU_XQG = 'XQG'
    """Tambor, plástico, cabeza extraíble"""
    CU_XQH = 'XQH'
    """Barril de madera con tapón"""
    CU_XQJ = 'XQJ'
    """Barril de madera con cabeza desprendible"""
    CU_XQK = 'XQK'
    """Bidón de acero con cabeza no desmontable"""
    CU_XQL = 'XQL'
    """Bidón de acero con cabeza desmontable"""
    CU_XQM = 'XQM'
    """Bidón de plástico con cabeza no desmontable"""
    CU_XQN = 'XQN'
    """Bidón de plástico con cabeza extraíble"""
    CU_XQP = 'XQP'
    """Caja de madera natural estándar"""
    CU_XQQ = 'XQQ'
    """Caja de madera natural con muros a prueba de filtraciones"""
    CU_XQR = 'XQR'
    """Caja de plástico expandida"""
    CU_XQS = 'XQS'
    """Caja de plástico sólida"""
    CU_XRD = 'XRD'
    """Rod"""
    CU_XRG = 'XRG'
    """Anillo"""
    CU_XRJ = 'XRJ'
    """Estante, Perchero para ropa"""
    CU_XRK = 'XRK'
    """Estante"""
    CU_XRL = 'XRL'
    """Carrete"""
    CU_XRO = 'XRO'
    """Rollo"""
    CU_XRT = 'XRT'
    """Red Roja"""
    CU_XRZ = 'XRZ'
    """Varillas  con fleje/ agrupados/ armados"""
    CU_XSA = 'XSA'
    """Saco"""
    CU_XSB = 'XSB'
    """Losa"""
    CU_XSC = 'XSC'
    """Cajón poco profundo"""
    CU_XSD = 'XSD'
    """Huso"""
    CU_XSE = 'XSE'
    """Baúl"""
    CU_XSH = 'XSH'
    """Bolsa pequeña hermética"""
    CU_XSI = 'XSI'
    """Patín"""
    CU_XSK = 'XSK'
    """Carcasa esqueleto"""
    CU_XSL = 'XSL'
    """Hoja de deslizamiento"""
    CU_XSM = 'XSM'
    """Hoja de metal"""
    CU_XSO = 'XSO'
    """Carrete pequeño"""
    CU_XSP = 'XSP'
    """Hoja de empaque de plástico"""
    CU_XSS = 'XSS'
    """Cajón de acero"""
    CU_XSU = 'XSU'
    """Maleta"""
    CU_XSV = 'XSV'
    """Sobre de acero"""
    CU_XSW = 'XSW'
    """Envoltorio"""
    CU_XSY = 'XSY'
    """Manga"""
    CU_XSZ = 'XSZ'
    """Hojas  con fleje/ agrupados/ armados"""
    CU_XT1 = 'XT1'
    """Tableta"""
    CU_XTB = 'XTB'
    """Tina"""
    CU_XTC = 'XTC'
    """Caja para té"""
    CU_XTD = 'XTD'
    """Tubo plegable"""
    CU_XTG = 'XTG'
    """Contenedor de tanque genérico"""
    CU_XTI = 'XTI'
    """Tierce"""
    CU_XTK = 'XTK'
    """Tanque rectangular"""
    CU_XTL = 'XTL'
    """Tina con tapa"""
    CU_XTN = 'XTN'
    """Hojalata"""
    CU_XTO = 'XTO'
    """Tonel"""
    CU_XTR = 'XTR'
    """Maletero"""
    CU_XTS = 'XTS'
    """Estructura"""
    CU_XTT = 'XTT'
    """Bolsa de mano"""
    CU_XTU = 'XTU'
    """Tubo"""
    CU_XTV = 'XTV'
    """Tubo con boquilla"""
    CU_XTW = 'XTW'
    """Pallet tricapa"""
    CU_XTY = 'XTY'
    """Tanque cilíndrico"""
    CU_XTZ = 'XTZ'
    """Tubos  con fleje/ agrupados/ armados"""
    CU_XUC = 'XUC'
    """Sin empaque"""
    CU_XUN = 'XUN'
    """Unidad"""
    CU_XVA = 'XVA'
    """Tanque"""
    CU_XVG = 'XVG'
    """Tanque de gas (a 1,031 mbar y 15° C)"""
    CU_XVI = 'XVI'
    """Frasco pequeño"""
    CU_XVK = 'XVK'
    """Paquete transportable"""
    CU_XVL = 'XVL'
    """Contenedor para líquidos a granel"""
    CU_XVN = 'XVN'
    """Vehículo"""
    CU_XVO = 'XVO'
    """Contenedor para sólido de partículas grandes a granel ("nódulos")"""
    CU_XVP = 'XVP'
    """Envasado al vacío"""
    CU_XVQ = 'XVQ'
    """Tanque para Gas licuado (a temperatura / presión anormal)"""
    CU_XVR = 'XVR'
    """Contenedor para sólidos de partículas granulares a granel (Granos)"""
    CU_XVS = 'XVS'
    """Contenedor de chatarra a granel"""
    CU_XVY = 'XVY'
    """Contenedor para sólido de partículas finas a granel ("polvos")"""
    CU_XWA = 'XWA'
    """Contenedor de granel intermedio"""
    CU_XWB = 'XWB'
    """Botella de mimbre"""
    CU_XWC = 'XWC'
    """Contenedor intermedio para gráneles y de acero"""
    CU_XWD = 'XWD'
    """Contenedor intermedio para gráneles y de aluminio"""
    CU_XWF = 'XWF'
    """Contenedor intermedio para gráneles y de metal"""
    CU_XWG = 'XWG'
    """Contenedor intermedio para gráneles y de acero presurizado menor a 10 kpa"""
    CU_XWH = 'XWH'
    """Contenedor intermedio para gráneles y de aluminio, presurizado menor a 10 kpa"""
    CU_XWJ = 'XWJ'
    """Contenedor intermedio para gráneles y de metal con una presión de 10 kpa"""
    CU_XWK = 'XWK'
    """Contenedor intermedio para gráneles y de acero para líquido"""
    CU_XWL = 'XWL'
    """Contenedor intermedio para gráneles y de aluminio para líquido"""
    CU_XWM = 'XWM'
    """Contenedor intermedio para gráneles y de metal para líquido"""
    CU_XWN = 'XWN'
    """Contenedor intermedio para gráneles con tejido plástico sin capa con revestimiento"""
    CU_XWP = 'XWP'
    """Contenedor intermedio para gráneles con tejido plástico y recubierto"""
    CU_XWQ = 'XWQ'
    """Contenedor intermedio para gráneles con tejido plástico con revestimiento"""
    CU_XWR = 'XWR'
    """Contenedor intermedio para gráneles con tejido plástico, revestido y con forro"""
    CU_XWS = 'XWS'
    """Contenedor intermedio para gráneles con película de plástico"""
    CU_XWT = 'XWT'
    """Contenedor intermedio para gráneles textil sin capa / forro"""
    CU_XWU = 'XWU'
    """Contenedor intermedio para gráneles de madera natural con forro interior"""
    CU_XWV = 'XWV'
    """Contenedor intermedio para gráneles textil recubierto"""
    CU_XWW = 'XWW'
    """Contenedor intermedio para gráneles textil con revestimiento"""
    CU_XWX = 'XWX'
    """Contenedor intermedio para gráneles textil recubierto y con forro"""
    CU_XWY = 'XWY'
    """Contenedor intermedio para gráneles contrachapado con revestimiento interior"""
    CU_XWZ = 'XWZ'
    """Contenedor intermedio para gráneles de madera reconstituida con revestimiento interior"""
    CU_XXA = 'XXA'
    """Bolsa de tejido plástico, sin abrigo interior ni forro"""
    CU_XXB = 'XXB'
    """Bolsa de tejido plástico a prueba de filtraciones"""
    CU_XXC = 'XXC'
    """Bolsa de tejido plástico resistente al agua"""
    CU_XXD = 'XXD'
    """Bolsa con película de plástico"""
    CU_XXF = 'XXF'
    """Bolsa textil sin capa ni forro interior"""
    CU_XXG = 'XXG'
    """Bolsa textil a prueba de filtraciones"""
    CU_XXH = 'XXH'
    """Bolsa textil resistente al agua"""
    CU_XXJ = 'XXJ'
    """Bolsa de papel multi-pared"""
    CU_XXK = 'XXK'
    """Bolsa de papel multi-pared, resistente al agua"""
    CU_XYA = 'XYA'
    """Empaque compuesto, recipiente de plástico en tambor de acero"""
    CU_XYB = 'XYB'
    """Empaque compuesto, recipiente de plástico en cajas de acero"""
    CU_XYC = 'XYC'
    """Empaque compuesto, recipiente de plástico en tambor de aluminio"""
    CU_XYD = 'XYD'
    """Empaque compuesto, recipiente de plástico en cajón de aluminio"""
    CU_XYF = 'XYF'
    """Empaque compuesto, recipiente de plástico en caja de madera"""
    CU_XYG = 'XYG'
    """Empaque compuesto, recipiente de plástico en tambor de madera contrachapada"""
    CU_XYH = 'XYH'
    """Empaque compuesto, recipiente de plástico en caja de madera contrachapada"""
    CU_XYJ = 'XYJ'
    """Empaque compuesto, recipiente de plástico en tambor de fibra"""
    CU_XYK = 'XYK'
    """Empaque compuesto, recipiente de plástico en caja de cartón"""
    CU_XYL = 'XYL'
    """Empaque compuesto, recipiente de plástico en el tambor de plástico"""
    CU_XYM = 'XYM'
    """Empaque compuesto, recipiente de plástico en caja de plástico sólido"""
    CU_XYN = 'XYN'
    """Empaque compuesto, receptáculo de vidrio en tambor de acero"""
    CU_XYP = 'XYP'
    """Empaque compuesto, receptáculo de vidrio en caja de cajas de acero"""
    CU_XYQ = 'XYQ'
    """Empaque compuesto, recipiente de vidrio en tambor de aluminio"""
    CU_XYR = 'XYR'
    """Empaque compuesto, receptáculo de vidrio en caja de aluminio"""
    CU_XYS = 'XYS'
    """Empaque compuesto, recipiente de vidrio en caja de madera"""
    CU_XYT = 'XYT'
    """Empaque compuesto, recipiente de vidrio en tambor de madera contrachapada"""
    CU_Xyv = 'Xyv'
    """Empaque compuesto, recipiente de vidrio en el cesto de mimbre"""
    CU_XYW = 'XYW'
    """Empaque compuesto, recipiente de vidrio en tambor de fibra"""
    CU_XYX = 'XYX'
    """Empaque compuesto, recipiente de vidrio en caja de cartón"""
    CU_XYY = 'XYY'
    """Empaque compuesto, recipiente de vidrio en paquete de plástico expandible"""
    CU_XYZ = 'XYZ'
    """Empaque compuesto, recipiente de vidrio en paquete de plástico sólido"""
    CU_XZA = 'XZA'
    """Contenedor de granel intermedio, papel, multi-pared"""
    CU_XZB = 'XZB'
    """Bolsa grande"""
    CU_XZC = 'XZC'
    """Contenedor intermedio para gráneles de papel, multi-pared y resistente al agua"""
    CU_XZD = 'XZD'
    """Contenedor intermedio para gráneles de plástico rígido, con equipo estructural para sólidos"""
    CU_XZF = 'XZF'
    """Contenedor intermedio para gráneles de plástico rígido, autoportante para sólidos"""
    CU_XZG = 'XZG'
    """Contenedor intermedio para gráneles de plástico rígido, con equipo estructural, presurizado"""
    CU_XZH = 'XZH'
    """Contenedor intermedio para gráneles de plástico rígido, autoportante y presurizado"""
    CU_XZJ = 'XZJ'
    """Contenedor intermedio para gráneles de plástico rígido, con equipo estructural para líquidos"""
    CU_XZK = 'XZK'
    """Contenedor intermedio para gráneles de plástico rígido, autoportante, líquidos"""
    CU_XZL = 'XZL'
    """Contenedor intermedio para gráneles, compuesto y de plástico rígido, sólidos"""
    CU_XZM = 'XZM'
    """Contenedor intermedio para gráneles, compuesto y de plástico flexible, sólidos"""
    CU_XZN = 'XZN'
    """Contenedor intermedio para gráneles, compuesto y de plástico rígido, presurizado"""
    CU_XZP = 'XZP'
    """Contenedor intermedio para gráneles, compuesto y de plástico flexible, presurizado"""
    CU_XZQ = 'XZQ'
    """Contenedor intermedio para gráneles, compuesto y de plástico rígido, líquidos"""
    CU_XZR = 'XZR'
    """Contenedor intermedio para gráneles, compuesto y de plástico flexible para líquidos"""
    CU_XZS = 'XZS'
    """Contenedor intermedio para gráneles, compuesto"""
    CU_XZT = 'XZT'
    """Contenedor intermedio para gráneles con tablero de fibras"""
    CU_XZU = 'XZU'
    """Contenedor intermedio para gráneles flexible"""
    CU_XZV = 'XZV'
    """Contenedor intermedio para gráneles de metal, distinto del acero"""
    CU_XZW = 'XZW'
    """Contenedor intermedio para gráneles, de madera natural"""
    CU_XZX = 'XZX'
    """Contenedor intermedio para gráneles, de contrachapado"""
    CU_XZY = 'XZY'
    """Contenedor intermedio para gráneles, de madera reconstituida"""
    CU_YDK = 'YDK'
    """Yarda cuadrada"""
    CU_YDQ = 'YDQ'
    """Yarda cúbica"""
    CU_YL = 'YL'
    """Cien yardas lineales"""
    CU_YRD = 'YRD'
    """Yarda"""
    CU_YT = 'YT'
    """Diez yardas"""
    CU_Z1 = 'Z1'
    """Furgoneta"""
    CU_Z11 = 'Z11'
    """Contenedor colgante"""
    CU_Z5 = 'Z5'
    """Arrastre"""
    CU_Z6 = 'Z6'
    """Punto de conferencia"""
    CU_Z8 = 'Z8'
    """Página de noticias"""
    CU_ZP = 'ZP'
    """Páginas"""
    CU_ZZ = 'ZZ'
    """Mutuamente definido"""
