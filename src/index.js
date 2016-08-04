import request from 'request';

request.get('http://www.google.com')
  .on('response', (response) => {
    console.log(response.statusCode);
  })
  .on('error', (err) => {
    console.error(err);
  });
