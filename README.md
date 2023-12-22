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

<strong>Response</strong>


```js
 200 - Éxito (Success)
```


Devuelve un JSON con una colección de las siguientes propiedades:


* `name:` El nombre de la carta.
* `price:` El precio de la carta.

```js
 400 - (Bad Request)
 500 - (Internal Server Error)
```



**Example**

Request:


```js
GET /price?name=Underground Sea
```

Response:


```js
[
  {
    "name": "Underground Sea",
    "price": 749.99
  },
  {
    "name": "Underground Sea",
    "price": 16999.99
  },
  {
    "name": "Underground Sea",
    "price": 8799.99
  },
  {
    "name": "Underground Sea",
    "price": 2099.99
  }
]
```
