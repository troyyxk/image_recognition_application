# API Documentation

[[_TOC_]]

## 0. Update History
| Date       | Description                                                  |
| ---------- | ------------------------------------------------------------ |
| 2021/11/24 | First version of API documentation.                          |
|            |                                                              |

## 1. Common rules
1. HTTP APIs.

2. API URLs should always end with a slash `/`. 

3. `Content-Type` of requests and responses are always `application/json` unless specified.

4. Structure of response.
```json
{
    "code": 0,
    "message": "OK",
    "result": ...
}
```
- Field `code` is the status code of each request processed, and should not be confused with HTTP status code. Normally, a `code` of `0` indicates that the request was processed as expected, and any `code` other than `0` should be regarded as an error.
- Field `message` gives the description of status code. This field is subjected to change, and should be used as information **ONLY** (i.e., do not determine any status by `message`.).
- Field `result` contains the data returned. See descriptions of each API below.

## 2. API List

### 3.1 Upload an image to create a recognition task.

#### Method and URL

```
HTTP POST
/api/upload/
```

#### Description

Receive an image from the browser, save it on the disk, create a record in the database, and send it to the task queue.

#### Request

##### Payload

An object with a property `image_b64` containing the Base64 encoded image data.

| Key         | Type   | Must be included? | Description                                                  | Example                                  |
| ----------- | ------ | ----------------- | ------------------------------------------------------------ | ---------------------------------------- |
| image_b64   | String | Y                 | Base64 encoded image data. The header (`data:image/jpeg;base64,`) **must be included** to specify the data type (`jpg`, `png`, etc...) of image. | "data:image/jpeg;base64,/9j/4AAQSkZJ..." |



#### Response

##### `result`

`uuid` of the uploaded `Image`.

#### Example

##### Request

```json
HTTP POST http://127.0.0.1:8000/api/upload/
Content-Type: application/json
Payload:
{
    "image_b64": "data:image/jpeg;base64,/9j/4AAQSkZJ..."
}
```

##### Response

```json
{
    "code": 0,
    "message": "OK",
    "result": {
        "uuid": "8d47cc5d-269e-4e5b-85ab-fd240a1bdb4e"
    }
}
```

### 3.2 Query the recognition result of an image.

#### Method and URL

```
HTTP GET
/api/query/{uuid}/
```

#### Description

Query the recognition result of an uploaded image, specified by its `uuid`. Returns the recognition result of the image. If the `uuid` does not exist, return error.

#### Response

##### `result`

An object containing:

| Key         | Type   | Must exist? | Can be null? | Description                                                  | Example                                |
| ----------- | ------ | ----------- | ------------ | ------------------------------------------------------------ | -------------------------------------- |
| uuid        | String | Y           | N            | `uuid` of `Image`.                                           | "8d47cc5d-269e-4e5b-85ab-fd240a1bdb4e" |
| image_url   | String | Y           | N            | URL of the image file.                                       | "http://127.0.0.1:8000/media/xxx.jpg"  |
| status      | Int    | Y           | N            | Status of the recognition task. Possible values are:<br />`0` - Waiting<br />`1` - Running<br />`2` - Finished<br />`3` - Failed | 2                                      |
| category    | String | Y           | Y            | Category with highest probability returned by GoogleNet.     | "goldfish"                             |
| probability | Float  | Y           | Y            | Probability (confidence) of the category.                    | 0.933                                  |



#### Example

##### Request

```json
HTTP GET http://127.0.0.1:8000/api/query/8d47cc5d-269e-4e5b-85ab-fd240a1bdb4e/
Content-Type: application/json
```

##### Response

```json
{
    "code": 0,
    "message": "OK",
    "result": {
        "uuid": "8d47cc5d-269e-4e5b-85ab-fd240a1bdb4e",
        "image_url": "http://127.0.0.1:8000/media/xxx.jpg",
        "status": 2,
        "catagory": "goldfish",
        "probability": 0.933
    }
}
```

