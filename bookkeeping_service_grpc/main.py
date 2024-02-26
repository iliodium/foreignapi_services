import os
import pickle
from concurrent import futures

import grpc

from config import CountWorkersService, BookkeepingServiceResponce, StatusServer
import structure_pb2 as pb2
import structure_pb2_grpc as pb2_grpc


class BookkeepingServiceServer(pb2_grpc.BookkeepingServiceServicer):
    def SendCheck(self, request, context):
        data: dict = pickle.loads(request.check)
        tax = int(sum(map(lambda x: x * 100, data.values())) * 0.87)

        return pb2.Response(
            answer=BookkeepingServiceResponce.pay_tax,
            tax=tax
        )


def run_server(url: str = "0.0.0.0:80"):
    print(StatusServer.start.format(BookkeepingServiceServer.__name__))
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=CountWorkersService.BookkeepingService))
    pb2_grpc.add_BookkeepingServiceServicer_to_server(BookkeepingServiceServer(), server)
    server.add_insecure_port(url)
    server.start()
    print(StatusServer.success.format(BookkeepingServiceServer.__name__))
    server.wait_for_termination()


if __name__ == '__main__':
    port = os.environ.get('PORT')
    URL = f"0.0.0.0:{port}"
    try:
        run_server(URL)
    except Exception as e:
        print(StatusServer.error.format(BookkeepingServiceServer.__name__))
        print(e)
