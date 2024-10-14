# SuperShop Management System

This project is a **Java-based SuperShop Management System** designed to streamline the management of products, clients, sales, and wastage for a retail environment. It features a secure login system, mail-sending functionality, and a user-friendly interface to access various management modules.

## Features

- **Login System**: Secure authentication to access the system's features.
- **Category Management**: Add, edit, and manage product categories.
- **Client Information**: Store and retrieve client information.
- **Sales Reporting**: View and generate sales reports to track business performance.
- **Product Information**: Manage inventory, including adding, updating, and deleting products.
- **Wastage Management**: Track product wastage and generate reports.
- **Mail Sending**: Send emails directly from the system, such as reports or notifications.
- **Exit**: Safely close the application.

## Modules Available After Logging In

1. **Category**: Manage product categories, such as adding new categories or editing existing ones.
2. **ClientInfo**: Store and manage client details, including contact information and purchase history.
3. **SalesReport**: View detailed sales reports, filter by date range, and export reports.
4. **ProductInfo**: Manage product details, including inventory levels, prices, and descriptions.
5. **Wastage**: Record product wastage and generate wastage reports.
6. **Mail**: Send emails, such as sales reports or updates, directly to clients or administrators.
7. **Exit**: Exit the application.

## Technologies Used

- **Java**: Core programming language used for the system.
- **Swing**: For the graphical user interface (GUI).
- **MySQL**: Database for storing product, client, and sales data.
- **JDBC**: Java API for connecting to the MySQL database.
- **JavaMail API**: For sending emails from within the application.

## Project Structure

  /project_root │ ├── /src # Java source code │ ├── login.java # Handles user login functionality │ ├── Category.java # Manages product categories │ ├── ClientInfo.java # Manages client information │ ├── SalesReport.java # Handles sales report generation │ ├── ProductInfo.java # Manages product details │ ├── Wastage.java # Handles wastage records │ ├── Mail.java # Sends emails using JavaMail API ├── /lib # External libraries ├── /db # Database scripts and configuration ├── README.md/ Project documentation

## Installation

### Prerequisites

- **Java Development Kit (JDK)** 8 or higher
- **MySQL** database
- **JDBC** connector for MySQL
- **JavaMail API** library
