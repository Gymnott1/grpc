import grpc
import test_pb2
import test_pb2_grpc
import time

def run_test():
    # Connect to the server
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = test_pb2_grpc.SpeedTestStub(channel)
        
        iterations = 2000
        print(f"Starting test: {iterations} calls...")
        
        start_time = time.time()
        
        for _ in range(iterations):
            # The actual gRPC call
            response = stub.SideTrip(test_pb2.PingRequest(data="ping"))
        
        end_time = time.time()
        
        # Calculations
        total_time = end_time - start_time
        rps = iterations / total_time
        latency = (total_time / iterations) * 1000 # in milliseconds

        print(f"--- Results ---")
        print(f"Total time: {total_time:.4f} seconds")
        print(f"Avg Latency: {latency:.4f} ms per call")
        print(f"Throughput: {rps:.2f} requests per second")

if __name__ == '__main__':
    run_test()
