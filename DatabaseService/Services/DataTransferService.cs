using Grpc.Core;
using MongoDB.Driver;

namespace DatabaseService.Services;

public class DataTransferService(IMongoCollection<DataTransferRecord> dataTransferRecords)
    : DataTransfer.DataTransferBase
{
    public override Task<Reply> Create(DataTransferRecord request, ServerCallContext context)
    {
        dataTransferRecords.InsertOne(request);
        return Task.FromResult(new Reply { Message = "Ok" });
    }

    public override Task<DataTransferRecord> Read(DataTransferRecordId request, ServerCallContext context)
    {
        var record = dataTransferRecords.Find(r => r.Id == request.Id).FirstOrDefault();
        return Task.FromResult(record);
    }

    public override Task<Reply> Update(DataTransferRecord request, ServerCallContext context)
    {
        dataTransferRecords.ReplaceOne(r => r.Id == request.Id, request);
        return Task.FromResult(new Reply { Message = "Ok" });
    }

    public override Task<Reply> Delete(DataTransferRecordId request, ServerCallContext context)
    {
        dataTransferRecords.DeleteOne(r => r.Id == request.Id);
        return Task.FromResult(new Reply { Message = "Ok" });
    }

    public override Task<Value> Min(Timestamp request, ServerCallContext context)
    {
        var min = dataTransferRecords.Find(r => r.Timestamp > request.Timestamp_).ToList()
            .Min(record => record.Bytes);
        return Task.FromResult(new Value { Value_ = min });
    }

    public override Task<Value> Max(Timestamp request, ServerCallContext context)
    {
        var max = dataTransferRecords.Find(r => r.Timestamp > request.Timestamp_).ToList()
            .Max(record => record.Bytes);
        return Task.FromResult(new Value { Value_ = max });
    }

    public override Task<Value> Avg(Timestamp request, ServerCallContext context)
    {
        var records = dataTransferRecords.Find(r => r.Timestamp > request.Timestamp_).ToList();
        return Task.FromResult(new Value { Value_ = (float)records.Average(record => record.Bytes) });
    }

    public override Task<Value> Sum(Timestamp request, ServerCallContext context)
    {
        int sum;
        try
        {
            sum = dataTransferRecords.Find(r => r.Timestamp > request.Timestamp_).ToList()
                .Sum(record => record.Bytes);
        }
        catch (OverflowException)
        {
            sum = int.MaxValue;
        }
        return Task.FromResult(new Value { Value_ = sum });
    }
}