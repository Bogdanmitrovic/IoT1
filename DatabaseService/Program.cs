using DatabaseService;
using DatabaseService.Services;
using MongoDB.Driver;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddGrpc();
var mongoClient = new MongoClient(builder.Configuration["ConnectionStrings:MongoDB"]);
var database = mongoClient.GetDatabase("DataTransferDatabase");
builder.Services.AddSingleton(database.GetCollection<DataTransferRecord>("DataTransferRecords"));

var app = builder.Build();

app.MapGrpcService<DataTransferService>();
app.MapGet("/",
    () =>
        "Communication with gRPC endpoints must be made through a gRPC client. To learn how to create a client, visit: https://go.microsoft.com/fwlink/?linkid=2086909");

app.Run();