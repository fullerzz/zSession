# from zconcurrent.zsession import zSession, RequestMap
# from typing import List
# import time
# import httpx

# requestMap = RequestMap(
#         url="http://localhost:8080/albums",
#         httpOperation="GET",
#     )

# sampleRequests: List[RequestMap] = []

# for i in range(5000):
#     sampleRequests.append(requestMap)


# def test_async_requests():
#     session = zSession(requestMaps=sampleRequests)
#     startTime = time.time()
#     responses = session.sendRequests()
#     endTime = time.time()
#     elapsedTime = endTime - startTime
#     print(f"Asynchronous operation completed {len(sampleRequests)} requests in {elapsedTime} seconds")
#     assert len(responses) != 0
#     assert elapsedTime < 1

# def test_sync_requests():
#     client = httpx.Client(transport=httpx.HTTPTransport(local_address="0.0.0.0"))
#     startTime = time.time()
#     for request in sampleRequests:
#         client.get(request.url)
#     endTime = time.time()
#     elapsedTime = endTime - startTime
#     print(f"Synchronous operation completed {len(sampleRequests)} requests in {elapsedTime} seconds")
#     assert elapsedTime < 3
