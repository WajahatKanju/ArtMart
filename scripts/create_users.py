# Import necessary models and constants
from users.models import (
    Seller,
    Customer,
    DeliveryDriver,
    Administrator,
    AffiliateMarketer,
    CustomerServiceRepresentative,
    MarketingManager,
    ProductManager,
    SocialMediaInfluencer,
    SalesRepresentative,
    LogisticsCoordinator,
    FinancialAnalyst,
    DataAnalyst,
    LegalCounsel,
    InventoryManager,
    User,
)

from users.constants import Role

# Create user instances for different roles
seller_user, _ = User.objects.get_or_create(
    first_name="Seller First Name",
    last_name="Seller Last Name",
    email="seller@example.com",
    role=Role.SELLER,
    phone="1234567890",
)

customer_user, _ = User.objects.get_or_create(
    first_name="Customer First Name",
    last_name="Customer Last Name",
    email="customer@example.com",
    role=Role.CUSTOMER,
    phone="9876543210",
)

driver_user, _ = User.objects.get_or_create(
    first_name="Driver First Name",
    last_name="Driver Last Name",
    email="driver@example.com",
    role=Role.DELIVERY_DRIVER,
    phone="5555555555",
)

admin_user, _ = User.objects.get_or_create(
    first_name="Admin First Name",
    last_name="Admin Last Name",
    email="admin@example.com",
    role=Role.ADMIN,
    phone="6666666666",
)

affiliate_marketer_user, _ = User.objects.get_or_create(
    first_name="Affiliate Marketer First Name",
    last_name="Affiliate Marketer Last Name",
    email="affiliate@example.com",
    role=Role.AFFILIATE_MARKETER,
    phone="7777777777",
)

# Repeat the process for other roles


marketing_manager_user, _ = User.objects.get_or_create(
    first_name="Marketing Manager First Name",
    last_name="Marketing Manager Last Name",
    email="marketing_manager@example.com",
    role=Role.MARKETING_MANAGER,
    phone="8888888888",
)

# Product Manager
product_manager_user, _ = User.objects.get_or_create(
    first_name="Product Manager First Name",
    last_name="Product Manager Last Name",
    email="product_manager@example.com",
    role=Role.PRODUCT_MANAGER,
    phone="9999999999",
)

# Social Media Influencer
social_media_influencer_user, _ = User.objects.get_or_create(
    first_name="Social Media Influencer First Name",
    last_name="Social Media Influencer Last Name",
    email="influencer@example.com",
    role=Role.SOCIAL_MEDIA_INFLUENCER,
    phone="1111111111",
)

# Sales Representative
sales_representative_user, _ = User.objects.get_or_create(
    first_name="Sales Representative First Name",
    last_name="Sales Representative Last Name",
    email="sales_rep@example.com",
    role=Role.SALES_REPRESENTATIVE,
    phone="2222222222",
)

# Logistics Coordinator
logistics_coordinator_user, _ = User.objects.get_or_create(
    first_name="Logistics Coordinator First Name",
    last_name="Logistics Coordinator Last Name",
    email="logistics@example.com",
    role=Role.LOGISTICS_COORDINATOR,
    phone="3333333333",
)

# Financial Analyst
financial_analyst_user, _ = User.objects.get_or_create(
    first_name="Financial Analyst First Name",
    last_name="Financial Analyst Last Name",
    email="financial_analyst@example.com",
    role=Role.FINANCIAL_ANALYST,
    phone="4444444444",
)

# Data Analyst
data_analyst_user, _ = User.objects.get_or_create(
    first_name="Data Analyst First Name",
    last_name="Data Analyst Last Name",
    email="data_analyst@example.com",
    role=Role.DATA_ANALYST,
    phone="5555555555",
)

# Legal Counsel
legal_counsel_user, _ = User.objects.get_or_create(
    first_name="Legal Counsel First Name",
    last_name="Legal Counsel Last Name",
    email="legal_counsel@example.com",
    role=Role.LEGAL_COUNSEL,
    phone="6666666666",
)

# Inventory Manager
inventory_manager_user, _ = User.objects.get_or_create(
    first_name="Inventory Manager First Name",
    last_name="Inventory Manager Last Name",
    email="inventory_manager@example.com",
    role=Role.INVENTORY_MANAGER,
    phone="7777777777",
)

# Repeat the process for other roles
# Create instances for Customer model
customer1 = Customer.objects.create(
    user=customer_user,
    shipping_address="Customer Address 1",
    billing_address="Billing Address 1",
    email_subscription=True,
)

# Create instances for DeliveryDriver model
driver1 = DeliveryDriver.objects.create(
    user=driver_user,
    license_number="License 1",
    vehicle_type="Vehicle Type 1",
    vehicle_registration_number="Vehicle Reg 1",
)

# Create instances for Administrator model
admin1 = Administrator.objects.create(user=admin_user)

# Create instances for AffiliateMarketer model
affiliate_marketer1 = AffiliateMarketer.objects.create(
    user=affiliate_marketer_user,
    marketing_campaign="Affiliate Campaign 1",
)

# Repeat the process for other roles
# Create instances for MarketingManager model
marketing_manager1 = MarketingManager.objects.create(
    user=marketing_manager_user,
    marketing_campaigns="Marketing Campaigns 1",
    marketing_budget=10000.00,
    marketing_strategy="Marketing Strategy 1",
)

# Create instances for ProductManager model
product_manager1 = ProductManager.objects.create(
    user=product_manager_user,
    product_categories="Product Categories 1",
    product_SKUs="Product SKUs 1",
    product_descriptions="Product Descriptions 1",
)

# Create instances for SocialMediaInfluencer model
social_media_influencer1 = SocialMediaInfluencer.objects.create(
    user=social_media_influencer_user,
    social_media_profiles="Social Media Profiles 1",
    follower_count=100000,
    engagement_metrics={"likes": 5000, "comments": 2000},
    content_type="Content Type 1",
)

# Repeat the process for other roles
# Create instances for SalesRepresentative model
sales_representative1 = SalesRepresentative.objects.create(
    user=sales_representative_user,
    sales_targets=1000,
)

# Create instances for LogisticsCoordinator model
logistics_coordinator1 = LogisticsCoordinator.objects.create(
    user=logistics_coordinator_user,
    shipping_methods="Shipping Methods 1",
    tracking_information="Tracking Information 1",
    delivery_schedules="Delivery Schedules 1",
)

# Create instances for FinancialAnalyst model
financial_analyst1 = FinancialAnalyst.objects.create(
    user=financial_analyst_user,
    financial_data={"revenue": 500000, "expenses": 300000},
    reports="Reports 1",
    forecasting_models="Forecasting Models 1",
)

# Create instances for DataAnalyst model
data_analyst1 = DataAnalyst.objects.create(
    user=data_analyst_user,
    data_sources="Data Sources 1",
    analysis_methodologies="Analysis Methodologies 1",
    reports_generated="Reports Generated 1",
)

# Create instances for LegalCounsel model
legal_counsel1 = LegalCounsel.objects.create(
    user=legal_counsel_user,
    legal_documents="Legal Documents 1",
    legal_cases="Legal Cases 1",
    legal_advice="Legal Advice 1",
)

# Create instances for InventoryManager model
inventory_manager1 = InventoryManager.objects.create(
    user=inventory_manager_user,
    inventory_tracking_data={"total_items": 1000, "in_stock": 500},
)
