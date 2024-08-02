# FastApi.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**readItemItemsItemIdGet**](DefaultApi.md#readItemItemsItemIdGet) | **GET** /items/{item_id} | Read Item
[**readRootGet**](DefaultApi.md#readRootGet) | **GET** / | Read Root
[**updateItemItemsItemIdPut**](DefaultApi.md#updateItemItemsItemIdPut) | **PUT** /items/{item_id} | Update Item



## readItemItemsItemIdGet

> Object readItemItemsItemIdGet(itemId, opts)

Read Item

### Example

```javascript
import FastApi from 'fast_api';

let apiInstance = new FastApi.DefaultApi();
let itemId = 56; // Number | 
let opts = {
  'q': "q_example" // String | 
};
apiInstance.readItemItemsItemIdGet(itemId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **itemId** | **Number**|  | 
 **q** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readRootGet

> Object readRootGet()

Read Root

### Example

```javascript
import FastApi from 'fast_api';

let apiInstance = new FastApi.DefaultApi();
apiInstance.readRootGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateItemItemsItemIdPut

> Object updateItemItemsItemIdPut(itemId, item)

Update Item

### Example

```javascript
import FastApi from 'fast_api';

let apiInstance = new FastApi.DefaultApi();
let itemId = 56; // Number | 
let item = new FastApi.Item(); // Item | 
apiInstance.updateItemItemsItemIdPut(itemId, item, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **itemId** | **Number**|  | 
 **item** | [**Item**](Item.md)|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

