# Tercera-pre-entrega-Cuello-Lopez

### 1. Pruebas

La preentrega consta de 3 modelos sobre especies del mercado de capitales

1.1. BONOS
1.2. ACCIONES
1.3. FUTUROS

Cada una tiene su forma particular de carga y contienen diferentes campos.

Para la prueba de la carga de cada una en particular primero debes realizar la baja de la preentrega en tu computadora.

Luego de eso correr el servidor de la entrega. Ya con el mismo podes ingresar en el vinculo del área superior derecha de la pantalla que dice "Especies".

Una vez dentro tendrás 3 botones que te dirigirán a 3 páginas diferentes para la carga de cada tipo de especie.

#### 1.1.BONOS

En la página de especies antes mencionada. Clickear en el botón que dice "Crear Bono". El mismo te dirigirá a una nueva página para realizar la carga de una nueva especie de bono.

##### 1.1.1 Campos Bonos

Los campos con los que cuenta son los siguientes:

1. Ticker: Es el acrónimo con el cual es identificado en el mercado (Ej. AL29D = Bono Argentina 2029 y la D de expresado en dólares). Consta de 5 carácteres alfanuméricos
2. Descripción: Brinda más detalle del ticker. Consta de hasta 30 carácteres alfanuméricos.
3. Cupón: Es el interés que paga el bono acordado en el momento de la emisión. Consta de decimales que detallan el monto de interés (entre 0.01 = 1% y 1 = 100%).
4. Emisor: Es el campo en el cual detallamos a qué empresa hace referencia el bono o si hace referencia a un estado Soberano (Ej. Argentina) o SubSoberano (Ej. Provincia de Córdoba). Consta de hasta 30 carácteres alfanuméricos.
5. Fecha de emisión: Fecha en la cual se emitió el bono. Fecha en formato (MM/DD/YYYY).
6. Fecha de vencimiento: Fecha en la cual venció el bono. Fecha en formato (MM/DD/YYYY).

##### 1.1.2 Prueba Bonos

Un ejemplo para probar esta funcionalidad podría ser:

Ticker: GD35D
Descripción: GLOBAL 2035
Cupón: 0.07
Emisor: ARGENTINA
Fecha de emisión: 7/9/2020
Fecha de vencimiento: 7/9/2035

Luego del ingreso de los datos, clickear en el botón crear. Esto generará la nueva especie y los redigirá a la página de "Listado de especies" donde verán esta nueva especie ya cargada.

#### 1.2.ACCIONES

En la página de especies antes mencionada. Clickear en el botón que dice "Crear Acción". El mismo te dirigirá a una nueva página para realizar la carga de una nueva especie de bono.

##### 1.2.1 Campos Acciones

Los campos con los que cuenta son los siguientes:

1. Ticker: Es el acrónimo con el cual es identificado en el mercado (Ej. GOOG = Alphabeth - Google). Consta de hasta 4 carácteres alfanuméricos
2. Descripción: Brinda más detalle del ticker y qué tipo de acción es (Ordinaria/Extraordinaria/Preferida). Consta de hasta 30 carácteres alfanuméricos.
3. Empresa: Hace referencia a la entidad que emitió la acción. Consta de hasta 20 carácteres alfanuméricos.

##### 1.2.2 Prueba Acciones

Un ejemplo para probar esta funcionalidad podría ser:

Ticker: BBAR
Descripción: Acc. Ord. Banco Francés
Empres: Banco Francés

Luego del ingreso de los datos, clickear en el botón crear. Esto generará la nueva especie y los redigirá a la página de "Listado de especies" donde verán esta nueva especie ya cargada.

#### 1.3.Futuros

En la página de especies antes mencionada. Clickear en el botón que dice "Crear Futuro". El mismo te dirigirá a una nueva página para realizar la carga de una nueva especie de bono.

##### 1.3.1 Campos Futuros

Los campos con los que cuenta son los siguientes:

1. Ticker: Es el acrónimo con el cual es identificado en el mercado (Ej. DLR072023 - Futuro de dólar a julio 2023). Consta de 9 carácteres alfanuméricos
2. Descripción: Brinda más detalle del ticker y qué tipo de acción es (Ordinaria/Extraordinaria/Preferida). Consta de hasta 30 carácteres alfanuméricos.
6. Fecha de vencimiento: Fecha en la cual venció el bono. Fecha en formato (MM/DD/YYYY).

##### 1.3.2 Prueba Acciones

Un ejemplo para probar esta funcionalidad podría ser:

Ticker: DLR102023
Descripción: FUT DOLAR OCT 2023
Empresa: 10/31/2023

Luego del ingreso de los datos, clickear en el botón crear. Esto generará la nueva especie y los redigirá a la página de "Listado de especies" donde verán esta nueva especie ya cargada.

#### 1.4 Listado de Especies

Para ir a esta página deben ingresar en el vinculo del área superior derecha de la pantalla que dice "Especies" que los llevará a la página del listado de especies. En ella de desplegarán todas las especies cargadas hasta el momento.

##### 1.4.1 Prueba Listado de especies

Para realizar la prueba de esta funcionalidad, dentro de la pantalla de listado de especies mencionada en el punto anterior deben ingresar el ticker buscado en el formulario y clickear en el botón "Buscar".

Una prueba sencilla es buscar "GD" y apareceran todos los bonos globales de Argentina ingresados hasta el momento.
