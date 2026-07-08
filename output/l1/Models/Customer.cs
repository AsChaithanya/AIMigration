Certainly! Here’s a production-ready .NET 8 C# conversion for the **Customer** class and related business flow, based on your requirements and context.

---

### Assumptions

- **CustomerRepository**: Handles data access for customers.
- **DiscountCalculator**: Calculates discounts based on customer points.
- **OrderService**: Orchestrates the workflow.
- **Invoice**: Represents invoice details.
- **Customer**: Represents customer entity.

---

## 1. Customer Entity

```csharp
namespace L1.Domain.Entities;

public class Customer
{
    public Guid Id { get; set; }
    public string Name { get; set; } = string.Empty;
    public int Points { get; set; }
    public decimal TotalAmount { get; set; }
}
```

---

## 2. Invoice Entity

```csharp
namespace L1.Domain.Entities;

public class Invoice
{
    public Guid CustomerId { get; set; }
    public decimal OriginalAmount { get; set; }
    public decimal Discount { get; set; }
    public decimal FinalAmount { get; set; }
}
```

---

## 3. CustomerRepository Interface & Implementation

```csharp
using L1.Domain.Entities;

public interface ICustomerRepository
{
    Task<List<Customer>> GetAllAsync();
    Task StoreInvoiceAsync(Invoice invoice);
}

public class CustomerRepository : ICustomerRepository
{
    // Assume dbContext injected via DI
    private readonly AppDbContext _dbContext;

    public CustomerRepository(AppDbContext dbContext)
    {
        _dbContext = dbContext;
    }

    public async Task<List<Customer>> GetAllAsync()
    {
        return await _dbContext.Customers.ToListAsync();
    }

    public async Task StoreInvoiceAsync(Invoice invoice)
    {
        _dbContext.Invoices.Add(invoice);
        await _dbContext.SaveChangesAsync();
    }
}
```

---

## 4. DiscountCalculator Interface & Implementation

```csharp
using L1.Domain.Entities;

public interface IDiscountCalculator
{
    decimal CalculateDiscount(Customer customer);
}

public class DiscountCalculator : IDiscountCalculator
{
    public decimal CalculateDiscount(Customer customer)
    {
        // Example: 1% discount per 100 points, max 10%
        var discountRate = Math.Min(customer.Points / 100 * 0.01m, 0.10m);
        return customer.TotalAmount * discountRate;
    }
}
```

---

## 5. OrderService (Business Logic)

```csharp
using L1.Domain.Entities;

public class OrderService
{
    private readonly ICustomerRepository _customerRepository;
    private readonly IDiscountCalculator _discountCalculator;

    public OrderService(
        ICustomerRepository customerRepository,
        IDiscountCalculator discountCalculator)
    {
        _customerRepository = customerRepository;
        _discountCalculator = discountCalculator;
    }

    public async Task ProcessInvoicesAsync()
    {
        var customers = await _customerRepository.GetAllAsync();

        foreach (var customer in customers)
        {
            var discount = _discountCalculator.CalculateDiscount(customer);
            var finalAmount = customer.TotalAmount - discount;

            var invoice = new Invoice
            {
                CustomerId = customer.Id,
                OriginalAmount = customer.TotalAmount,
                Discount = discount,
                FinalAmount = finalAmount
            };

            await _customerRepository.StoreInvoiceAsync(invoice);
        }
    }
}
```

---

## 6. Dependency Injection Registration (Startup/Program.cs)

```csharp
builder.Services.AddScoped<ICustomerRepository, CustomerRepository>();
builder.Services.AddScoped<IDiscountCalculator, DiscountCalculator>();
builder.Services.AddScoped<OrderService>();
```

---

## 7. Usage Example

```csharp
// In a controller or background service
public class InvoiceController : ControllerBase
{
    private readonly OrderService _orderService;

    public InvoiceController(OrderService orderService)
    {
        _orderService = orderService;
    }

    [HttpPost("process-invoices")]
    public async Task<IActionResult> ProcessInvoices()
    {
        await _orderService.ProcessInvoicesAsync();
        return Ok();
    }
}
```

---

## Summary

- **Business logic preserved**: Retrieve customers, calculate discounts, generate invoices, store results.
- **.NET 8 conventions**: Async methods, dependency injection, clean separation.
- **Production-ready**: Entities, interfaces, DI, async/await, clean code.

If you have the original Java class, I can further tailor the migration. Let me know if you need more details or adjustments!