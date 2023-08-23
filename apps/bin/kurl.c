
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <curl/curl.h>

#define URL "http://localhost:7860/api"

struct ResponseData
{
  char *data;
  size_t size;
};

void initResponseData(struct ResponseData *responseData)
{
  responseData->size = 0;
  responseData->data = malloc(responseData->size + 1);
  if (!responseData->data)
  {
    perror("malloc() failed");
    exit(EXIT_FAILURE);
  }
  responseData->data[0] = '\0';
}

size_t curlWriteMemoryCallback(void *ptr, size_t size, size_t nmemb, void *userData)
{
  struct ResponseData *responseData = (struct ResponseData *)userData;
  size_t new_size = responseData->size + size * nmemb;
  responseData->data = realloc(responseData->data, new_size + 1);
  if (!responseData->data)
  {
    perror("realloc() failed");
    exit(EXIT_FAILURE);
  }
  memcpy(responseData->data + responseData->size, ptr, size * nmemb);
  responseData->data[new_size] = '\0';
  responseData->size = new_size;
  return size * nmemb;
}

int main(void)
{
  CURL *curl;
  CURLcode res;
  struct ResponseData responseData;

  initResponseData(&responseData);

  curl_global_init(CURL_GLOBAL_DEFAULT);

  curl = curl_easy_init();
  if (!curl)
  {
    fprintf(stderr, "Failed to initialize libcurl\n");
    return EXIT_FAILURE;
  }

  struct curl_slist *headers = NULL;
  headers = curl_slist_append(headers, "Content-Type: application/json");

  char *data = "{\"model\": \"orca-mini-7b.ggmlv3.q4_0.bin\", \"prompt\": [\"Write a python program which provides the dot product of its arguments using no imports\"]}";
  /* curl_easy  */
  curl_easy_setopt(curl, CURLOPT_URL, URL);
  curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
  curl_easy_setopt(curl, CURLOPT_POSTFIELDS, data);
  curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, curlWriteMemoryCallback);
  curl_easy_setopt(curl, CURLOPT_WRITEDATA, &responseData);

  res = curl_easy_perform(curl);
  if (res != CURLE_OK)
  {
    fprintf(stderr, "cURL error: %s\n", curl_easy_strerror(res));
    curl_easy_cleanup(curl);
    curl_slist_free_all(headers);
    free(responseData.data);
    curl_global_cleanup();
    return EXIT_FAILURE;
  }

  printf("%s\n", responseData.data);

  curl_easy_cleanup(curl);
  curl_slist_free_all(headers);
  free(responseData.data);
  curl_global_cleanup();

  return EXIT_SUCCESS;
}