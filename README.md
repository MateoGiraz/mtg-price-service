# Setup

## Instalar dependencias
```js
pip install -r .\requirements.txt 
``` 
## Quick start

```js
python -m uvicorn main:app --reload
```
# API docs
> :warning: **Por el momento no se puede filtrar según el estado de la carta**

## **Price**


```js
BaseURL: /price
```



```js
GET /price
```


Devuelve los precios de las cartas con igual nombre al parámetro name recibido

**Parameters**



* <code>name<strong></strong></code> (requerido): El nombre de la carta.
* <code>edition<strong></strong></code> (opcional): La edición de la carta.

<strong>Response</strong>


```js
 200 - Éxito (Success)
```


Devuelve un JSON con una colección de las siguientes propiedades:


* `name:` El nombre de la carta.
* `price:` El precio de la carta.
* `edition:` La edición de la carta.

```js
 400 - (Bad Request)
 500 - (Internal Server Error)
```



**Example**

Request:


```js
GET /price?name=Underground%Sea
```

Response:


```js
[
  {
    "name": "Underground Sea",
    "prices": {
      "nm": 749.99,
      "ex": 674.99,
      "vg": 599.99,
      "g": 524.99
    },
    "edition": "3rd Edition"
  },
  {
    "name": "Underground Sea",
    "prices": {
      "nm": 16999.99,
      "ex": 13599.99,
      "vg": 10199.99,
      "g": 6800.0
    },
    "edition": "Alpha"
  },
  {
    "name": "Underground Sea",
    "prices": {
      "nm": 8799.99,
      "ex": 7039.99,
      "vg": 5279.99,
      "g": 3520.0
    },
    "edition": "Beta"
  },
  {
    "name": "Underground Sea",
    "prices": {
      "nm": 2099.99,
      "ex": 1679.99,
      "vg": 1259.99,
      "g": 840.0
    },
    "edition": "Unlimited"
  }
]
```

**Example**

Request:


```js
GET /price?name=Underground%Sea&edition=Beta
```

Response:


```js
[
  {
    "name": "Underground Sea",
    "prices": {
      "nm": 8799.99,
      "ex": 7039.99,
      "vg": 5279.99,
      "g": 3520.0
    },
    "edition": "Beta"
  },
]
```

