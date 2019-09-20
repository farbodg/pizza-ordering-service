INSERT INTO pizzaapp_ingredient (display_name, code, price)
VALUES
('Pepperoni', 'PEPPERONI', '1.00'),
('Ground Beef', 'GROUNDBEEF', '1.25'),
('White Onion', 'ONION', '0.25'),
('Green Pepper', 'GREENPEP', '0.50'),
('Pineapple', 'PINEAPPLE', '0.45'),
('Red Tomato', 'TOMATO', '0.60'),
('White Mushroom', 'MUSHROOM', '0.35');

INSERT INTO pizzaapp_orderstatus (label)
VALUES
('Placed'),
('Processing'),
('Ready'),
('Delivering'),
('Delivered'),
('CustomerPickedUp'),
('Cancelled');

INSERT INTO pizzaapp_customer (first_name, last_name, address, phone_number)
VALUES
('customer', 'one', '123 Ohlauerstr, Berlin DE', '+49 123 4567890'),
('customer', 'two', '228 E 8th Avenue, Vancouver BC', '1 604 12345678');