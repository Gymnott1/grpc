import grpc
from concurrent import futures
import test_pb2
import test_pb2_grpc

class SpeedTestServicer(test_pb2_grpc.SpeedTestServicer):
    def SideTrip(self, request, context):
        return test_pb2.PongResponse(message="ACK")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    test_pb2_grpc.add_SpeedTestServicer_to_server(SpeedTestServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("Server started on port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
