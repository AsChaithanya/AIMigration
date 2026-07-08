Certainly! Here’s a production-ready .NET 8 C# version of the **OrderService** class, based on your requirements and relationships.

---

### Java Class (for reference)

```java
public class OrderService {
    private CustomerRepository customerRepository;
    private DiscountCalculator discountCalculator;

    public OrderService(CustomerRepository customerRepository, DiscountCalculator discountCalculator) {
        this.customerRepository = customerRepository;
        this.discountCalculator = discountCalculator;
    }

    public void processOrders() {
        List<Customer> customers = customerRepository.getCustomers();
        for (Customer customer : customers) {
            double discount = discountCalculator.calculateDiscount(customer);
            Invoice invoice = generateInvoice(customer, discount);
            storeInvoice(invoice);
        }
    }

    private Invoice generateInvoice(Customer customer, double discount) {
        // Business logic to generate invoice
    }

    private void storeInvoice(Invoice invoice) {
        // Business logic to store invoice
    }
}
```

---

## .NET 8 C# Migration

### 1. Interfaces

```csharp
public interface ICustomerRepository
{
    IEnumerable<Customer> GetCustomers();
}

public interface IDiscountCalculator
{
    decimal CalculateDiscount(Customer customer);
}
```

### 2. Models

```csharp
public class Customer
{
    // Properties as needed
}

public class Invoice
{
    // Properties as needed
}
```

### 3. OrderService

```csharp
using System.Collections.Generic;

public class OrderService
{
    private readonly ICustomerRepository _customerRepository;
    private readonly IDiscountCalculator _discountCalculator;

    public OrderService(ICustomerRepository customerRepository, IDiscountCalculator discountCalculator)
    {
        _customerRepository = customerRepository ?? throw new ArgumentNullException(nameof(customerRepository));
        _discountCalculator = discountCalculator ?? throw new ArgumentNullException(nameof(discountCalculator));
    }

    public void ProcessOrders()
    {
        var customers = _customerRepository.GetCustomers();

        foreach (var customer in customers)
        {
            var discount = _discountCalculator.CalculateDiscount(customer);
            var invoice = GenerateInvoice(customer, discount);
            StoreInvoice(invoice);
        }
    }

    private Invoice GenerateInvoice(Customer customer, decimal discount)
    {
        // Business logic to generate invoice
        // Example:
        return new Invoice
        {
            // Fill properties based on customer and discount
        };
    }

    private void StoreInvoice(Invoice invoice)
    {
        // Business logic to store invoice
        // Example: Save to database or file system
    }
}
```

---

### 4. Dependency Injection Registration (e.g., in Program.cs)

```csharp
builder.Services.AddScoped<ICustomerRepository, CustomerRepository>();
builder.Services.AddScoped<IDiscountCalculator, DiscountCalculator>();
builder.Services.AddScoped<OrderService>();
```

---

## Key Points

- **Dependency Injection:** Uses constructor injection for dependencies.
- **.NET 8 conventions:** Uses interfaces, `IEnumerable<T>`, and `decimal` for monetary values.
- **Business Logic:** Preserved in `GenerateInvoice` and `StoreInvoice` methods.
- **Clean Code:** Follows C# naming conventions and best practices.

---

**If you need implementations for `CustomerRepository`, `DiscountCalculator`, or want async support, let me know!**