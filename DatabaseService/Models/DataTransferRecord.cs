namespace DatabaseService.Models;

public class DataTransferRecord
{
    public int Id { get; set; } = -1;
    public int Bytes { get; set; } = 0;
    public int Packets { get; set; } = 0;
    public int Timestamp { get; set; } = -1;
}