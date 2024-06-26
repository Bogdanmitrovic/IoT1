# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import datatransfer_pb2 as datatransfer__pb2


class DataTransferStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/dt.DataTransfer/Create',
                request_serializer=datatransfer__pb2.DataTransferRecord.SerializeToString,
                response_deserializer=datatransfer__pb2.Reply.FromString,
                )
        self.Read = channel.unary_unary(
                '/dt.DataTransfer/Read',
                request_serializer=datatransfer__pb2.DataTransferRecordId.SerializeToString,
                response_deserializer=datatransfer__pb2.DataTransferRecord.FromString,
                )
        self.Update = channel.unary_unary(
                '/dt.DataTransfer/Update',
                request_serializer=datatransfer__pb2.DataTransferRecord.SerializeToString,
                response_deserializer=datatransfer__pb2.Reply.FromString,
                )
        self.Delete = channel.unary_unary(
                '/dt.DataTransfer/Delete',
                request_serializer=datatransfer__pb2.DataTransferRecordId.SerializeToString,
                response_deserializer=datatransfer__pb2.Reply.FromString,
                )
        self.Min = channel.unary_unary(
                '/dt.DataTransfer/Min',
                request_serializer=datatransfer__pb2.Timestamp.SerializeToString,
                response_deserializer=datatransfer__pb2.Value.FromString,
                )
        self.Max = channel.unary_unary(
                '/dt.DataTransfer/Max',
                request_serializer=datatransfer__pb2.Timestamp.SerializeToString,
                response_deserializer=datatransfer__pb2.Value.FromString,
                )
        self.Avg = channel.unary_unary(
                '/dt.DataTransfer/Avg',
                request_serializer=datatransfer__pb2.Timestamp.SerializeToString,
                response_deserializer=datatransfer__pb2.Value.FromString,
                )
        self.Sum = channel.unary_unary(
                '/dt.DataTransfer/Sum',
                request_serializer=datatransfer__pb2.Timestamp.SerializeToString,
                response_deserializer=datatransfer__pb2.Value.FromString,
                )


class DataTransferServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Read(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Min(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Max(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Avg(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Sum(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataTransferServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=datatransfer__pb2.DataTransferRecord.FromString,
                    response_serializer=datatransfer__pb2.Reply.SerializeToString,
            ),
            'Read': grpc.unary_unary_rpc_method_handler(
                    servicer.Read,
                    request_deserializer=datatransfer__pb2.DataTransferRecordId.FromString,
                    response_serializer=datatransfer__pb2.DataTransferRecord.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=datatransfer__pb2.DataTransferRecord.FromString,
                    response_serializer=datatransfer__pb2.Reply.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=datatransfer__pb2.DataTransferRecordId.FromString,
                    response_serializer=datatransfer__pb2.Reply.SerializeToString,
            ),
            'Min': grpc.unary_unary_rpc_method_handler(
                    servicer.Min,
                    request_deserializer=datatransfer__pb2.Timestamp.FromString,
                    response_serializer=datatransfer__pb2.Value.SerializeToString,
            ),
            'Max': grpc.unary_unary_rpc_method_handler(
                    servicer.Max,
                    request_deserializer=datatransfer__pb2.Timestamp.FromString,
                    response_serializer=datatransfer__pb2.Value.SerializeToString,
            ),
            'Avg': grpc.unary_unary_rpc_method_handler(
                    servicer.Avg,
                    request_deserializer=datatransfer__pb2.Timestamp.FromString,
                    response_serializer=datatransfer__pb2.Value.SerializeToString,
            ),
            'Sum': grpc.unary_unary_rpc_method_handler(
                    servicer.Sum,
                    request_deserializer=datatransfer__pb2.Timestamp.FromString,
                    response_serializer=datatransfer__pb2.Value.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dt.DataTransfer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DataTransfer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dt.DataTransfer/Create',
            datatransfer__pb2.DataTransferRecord.SerializeToString,
            datatransfer__pb2.Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Read(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dt.DataTransfer/Read',
            datatransfer__pb2.DataTransferRecordId.SerializeToString,
            datatransfer__pb2.DataTransferRecord.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dt.DataTransfer/Update',
            datatransfer__pb2.DataTransferRecord.SerializeToString,
            datatransfer__pb2.Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dt.DataTransfer/Delete',
            datatransfer__pb2.DataTransferRecordId.SerializeToString,
            datatransfer__pb2.Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Min(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dt.DataTransfer/Min',
            datatransfer__pb2.Timestamp.SerializeToString,
            datatransfer__pb2.Value.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Max(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dt.DataTransfer/Max',
            datatransfer__pb2.Timestamp.SerializeToString,
            datatransfer__pb2.Value.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Avg(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dt.DataTransfer/Avg',
            datatransfer__pb2.Timestamp.SerializeToString,
            datatransfer__pb2.Value.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Sum(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dt.DataTransfer/Sum',
            datatransfer__pb2.Timestamp.SerializeToString,
            datatransfer__pb2.Value.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
