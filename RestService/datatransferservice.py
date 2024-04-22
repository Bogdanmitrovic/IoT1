from flask import Flask, jsonify, request
import grpc
import datatransfer_pb2
import datatransfer_pb2_grpc

app = Flask(__name__)

@app.route('/api/datatransfer', methods=['GET'])
def get_record():
    try:
        #with grpc.insecure_channel('localhost:8080') as channel:
        with grpc.insecure_channel('172.18.0.3:8080') as channel:
            stub = datatransfer_pb2_grpc.DataTransferStub(channel)
            recordid = int(request.args.get('recordid'))
            record = stub.Read(datatransfer_pb2.DataTransferRecordId(id=recordid))
            recstr=str(record)
            return recstr
    except Exception as e:
        return jsonify({'message': f"Error: {e}"})

@app.route('/api/datatransfer', methods=['POST'])
def post_record():
    try:
        #with grpc.insecure_channel('172.18.0.3:8080') as channel:
        with grpc.insecure_channel('172.18.0.3:8080') as channel:
            stub = datatransfer_pb2_grpc.DataTransferStub(channel)
            record = request.get_json()
            print(record)
            recordstub=datatransfer_pb2.DataTransferRecord(id=record['_id'], bytes=record['Bytes'], packets=record['Packets'], timestamp=record['Timestamp'])
            reply = stub.Create(recordstub)
            return str(reply)
    except Exception as e:
        return jsonify({'message': f"Error: {e}"})

@app.route('/api/datatransfer', methods=['PUT'])
def put_record():
    try:
        #with grpc.insecure_channel('172.18.0.3:8080') as channel:
        with grpc.insecure_channel('172.18.0.3:8080') as channel:
            stub = datatransfer_pb2_grpc.DataTransferStub(channel)
            record = request.get_json()
            print(record)
            recordstub=datatransfer_pb2.DataTransferRecord(id=record['_id'], bytes=record['Bytes'], packets=record['Packets'], timestamp=record['Timestamp'])
            reply = stub.Update(recordstub)
            return str(reply)
    except Exception as e:
        return jsonify({'message': f"Error: {e}"})

@app.route('/api/datatransfer', methods=['DELETE'])
def delete_record():
    try:
        with grpc.insecure_channel('172.18.0.3:8080') as channel:
            stub = datatransfer_pb2_grpc.DataTransferStub(channel)
            recordid = int(request.args.get('recordid'))
            reply = stub.Delete(datatransfer_pb2.DataTransferRecordId(id=recordid))
            return str(reply)
    except Exception as e:
        return jsonify({'message': f"Error: {e}"})

@app.route('/api/datatransfermax', methods=['GET'])
def max():
    try:
        with grpc.insecure_channel('172.18.0.3:8080') as channel:
            stub = datatransfer_pb2_grpc.DataTransferStub(channel)
            tstamp = int(request.args.get('timestamp'))
            reply = stub.Max(datatransfer_pb2.Timestamp(timestamp=tstamp))
            return str(reply)
    except Exception as e:
        return jsonify({'message': f"Error: {e}"})

@app.route('/api/datatransfermin', methods=['GET'])
def min():
    try:
        with grpc.insecure_channel('172.18.0.3:8080') as channel:
            stub = datatransfer_pb2_grpc.DataTransferStub(channel)
            tstamp = int(request.args.get('timestamp'))
            reply = stub.Min(datatransfer_pb2.Timestamp(timestamp=tstamp))
            return str(reply)
    except Exception as e:
        return jsonify({'message': f"Error: {e}"})

@app.route('/api/datatransferavg', methods=['GET'])
def avg():
    try:
        with grpc.insecure_channel('172.18.0.3:8080') as channel:
            stub = datatransfer_pb2_grpc.DataTransferStub(channel)
            tstamp = int(request.args.get('timestamp'))
            reply = stub.Avg(datatransfer_pb2.Timestamp(timestamp=tstamp))
            return str(reply)
    except Exception as e:
        return jsonify({'message': f"Error: {e}"})

@app.route('/api/datatransfersum', methods=['GET'])
def sum():
    try:
        with grpc.insecure_channel('172.18.0.3:8080') as channel:
            stub = datatransfer_pb2_grpc.DataTransferStub(channel)
            tstamp = int(request.args.get('timestamp'))
            reply = stub.Sum(datatransfer_pb2.Timestamp(timestamp=tstamp))
            return str(reply)
    except Exception as e:
        return jsonify({'message': f"Error: {e}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)
# export requirements to requirements.txt
