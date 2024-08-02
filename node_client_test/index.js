var FastApi = require('fast_api');


var api = new FastApi.DefaultApi()
var itemId = 56; // {Number} 
var opts = {
  'q': "q_example" // {String} 
};
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.readItemItemsItemIdGet(itemId, opts, callback);
