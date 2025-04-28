import subprocess
import os

def generate_uml_diagram():
    # PlantUML syntax for the UML diagram (same as in the Java code)
    source = """@startuml
skinparam class {
    BackgroundColor White
    BorderColor Black
    ArrowColor Black
}

abstract class User {
    -user_id: int
    -firstName: string
    -lastName: string
    -email: string
    -password: string
    -contactNumber: string
    -createdAt: datetime
    +register()
    +login()
    +updateProfile()
    +resetPassword()
}

class Customer {
    -customerId: int
    -address: string
    -paymentInfo: string
    +viewProducts()
    +searchProducts()
    +addToCart()
    +checkout()
    +trackOrder()
    +provideFeedback()
}

class Admin {
    -adminId: int
    -role: string
    +manageProducts()
    +manageCategories()
    +manageOrders()
    +viewReports()
}

class Cart {
    -cartId: int
    -customerId: int
    -totalAmount: float
    -createdAt: datetime
    -updatedAt: datetime
    +addItem()
    +removeItem()
    +updateQuantity()
    +calculateTotal()
    +checkout()
}

class CartItem {
    -cartItemId: int
    -cartId: int
    -orderId: int
    -productId: int
    -quantity: int
    -price: float
    +updateQuantity()
    +calculateSubtotal()
}

class Order {
    -orderId: int
    -customerId: int
    -orderDate: datetime
    -createdAt: datetime
    -totalAmount: float
    -shippingAddress: string
    -status: string
    -paymentMethod: string
    -paymentStatus: string
    +calculateTotal()
    +updateStatus()
    +generateInvoice()
}

class OrderItem {
    -orderItemId: int
    -orderId: int
    -productId: int
    -quantity: int
    -price: float
}

class Product {
    -productId: int
    -name: string
    -description: string
    -price: float
    -stock: int
    -imageUrl: string
    -categoryId: int
    -rating: float
    -createdAt: datetime
    -updatedAt: datetime
    +displayDetails()
    +updateStock()
}

class Category {
    -categoryId: int
    -name: string
    -description: string
    +displayProducts()
}

class Feedback {
    -feedbackId: int
    -customerId: int
    -productId: int
    -rating: int
    -comment: string
    -createdAt: datetime
    +submitFeedback()
}

class Payment {
    -paymentId: int
    -orderId: int
    -amount: float
    -paymentMethod: string
    -paymentStatus: string
    -timestamp: datetime
    +processPayment()
    +verifyPayment()
    +generateReceipt()
}

User <|-- Customer : <color:blue>extends</color>
User <|-- Admin : <color:blue>extends</color>
Customer --> "1" Cart : <color:blue>places</color>
Cart --> "1..*" CartItem : <color:blue>contains</color>
CartItem --> "1" Product : <color:blue>references</color>
Customer --> "1..*" Order : <color:blue>places</color>
Order --> "1..*" OrderItem : <color:blue>has</color>
OrderItem --> "1" Product : <color:blue>references</color>
Order --> "1" Payment : <color:blue>manages</color>
Product --> "1" Category : <color:blue>belongs to</color>
Customer --> "0..*" Feedback : <color:blue>provides</color>
Feedback --> "1" Product : <color:blue>references</color>
Admin --> "0..*" Product : <color:blue>manages</color>
Admin --> "0..*" Order : <color:blue>manages</color>
@enduml"""

    # Write the PlantUML source to a temporary file
    temp_file = "uml_diagram.txt"
    with open(temp_file, "w") as f:
        f.write(source)

    # Run PlantUML using the local plantuml.jar to generate the diagram
    try:
        # Command to run plantuml.jar
        # Assumes plantuml.jar is in the current directory
        result = subprocess.run(
            ["java", "-jar", "plantuml.jar", temp_file],
            capture_output=True,
            text=True
        )
        
        # Check if the command was successful
        if result.returncode == 0:
            # PlantUML generates uml_diagram.png by default from uml_diagram.txt
            if os.path.exists("uml_diagram.png"):
                print("UML diagram generated as uml_diagram.png")
            else:
                print("Error: uml_diagram.png was not generated.")
        else:
            print(f"Error running PlantUML: {result.stderr}")
    except Exception as e:
        print(f"Error generating UML diagram: {e}")
    finally:
        # Clean up the temporary file
        if os.path.exists(temp_file):
            os.remove(temp_file)

if __name__ == "__main__":
    generate_uml_diagram()
