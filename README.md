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



* <code>name (string)<strong></strong></code> (requerido): El nombre de la carta.
* <code>edition (string)<strong></strong></code> (opcional): La edición de la carta.
* <code>foil (bool)<strong></strong></code> (opcional): La característica foil de la carta.

<strong>Response</strong>


```js
 200 - Éxito (Success)
```


Devuelve un JSON con una colección de las siguientes propiedades:


```js
"name": "El nombre de la carta",
"edition": "La edición de la carta",
"foil": "La característica foil de la carta",
"prices": {
  "nm": 0,
  "ex": 0,
  "vg": 0,
  "g": 0,
}
```

```js
 400 - (Bad Request)
 500 - (Internal Server Error)
```


**Example**

Request:


```js
GET /price?name=Goblin Matron
```

Response:


```js
[
  {
    "name": "Goblin Matron",
    "edition": "Dominaria Remastered",
    "foil": false,
    "prices": {
      "nm": 0.35,
      "ex": 0.28,
      "vg": 0.25,
      "g": 0.18
    }
  },
  {
    "name": "Goblin Matron",
    "edition": "Portal II",
    "foil": false,
    "prices": {
      "nm": 2.99,
      "ex": 2.39,
      "vg": 2.09,
      "g": 1.5
    }
  },
  {
    "name": "Goblin Matron",
    "edition": "Modern Horizons",
    "foil": false,
    "prices": {
      "nm": 0.35,
      "ex": 0.28,
      "vg": 0.25,
      "g": 0.18
    }
  },
  {
    "name": "Goblin Matron",
    "edition": "Anthologies",
    "foil": false,
    "prices": {
      "nm": 0.59,
      "ex": 0.47,
      "vg": 0.41,
      "g": 0.3
    }
  }
]
```

**Example**

Request:


```js
GET /price?name=Goblin Matron&edition=Modern Horizons&foil=true
```

Response:


```js
[
  {
    "name": "Goblin Matron",
    "edition": "Modern Horizons",
    "foil": true,
    "prices": {
      "nm": 1.49,
      "ex": 1.19,
      "vg": 0.89,
      "g": 0.6
    }
  }
]
```

