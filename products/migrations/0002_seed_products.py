from django.db import migrations

def seed_data(apps, schema_editor):
    Category = apps.get_model('products', 'Category')
    Product = apps.get_model('products', 'Product')

    # Create Categories
    linux_cat = Category.objects.create(name='Linux & Open Source', slug='linux')
    ms_cat = Category.objects.create(name='Microsoft & Windows', slug='microsoft')
    mac_cat = Category.objects.create(name='Mac & Apple Silicon', slug='mac')

    # Linux products (9 products)
    Product.objects.bulk_create([
        Product(
            category=linux_cat,
            name='Laptop ThinkPad - Ubuntu Edition',
            description='Pre-instalada con Ubuntu 24.04 LTS y drivers optimizados.',
            price=850000,
            stock=10,
            image_url='https://images.unsplash.com/photo-1588505794452-9e58a44a551f?auto=format&fit=crop&w=800&q=80'
        ),
        Product(
            category=linux_cat,
            name='Raspberry Pi 5 - 8GB RAM',
            description='El cerebro perfecto para tu servidor Linux casero o proyectos IoT.',
            price=95000,
            stock=15,
            image_url='https://images.unsplash.com/photo-1555664424-778a1e5e1b48?auto=format&fit=crop&w=800&q=80'
        ),
        Product(
            category=linux_cat,
            name='Flipper Zero',
            description='Multi-herramienta para geeks y entusiastas del hardware hacking.',
            price=180000,
            stock=5,
            image_url='https://images.unsplash.com/photo-1629654297299-c8506221ca97?auto=format&fit=crop&w=800&q=80'
        ),
        Product(
            category=linux_cat,
            name='Mini Servidor Proxmox',
            description='Hardware compacto listo para virtualización y contenedores Docker.',
            price=420000,
            stock=8,
            image_url='https://images.unsplash.com/photo-1551434678-e076c223a692?auto=format&fit=crop&w=800&q=80'
        ),
        Product(
            category=linux_cat,
            name='Router OpenWrt Ready',
            description='Router de alta gama con firmware libre para control total de red.',
            price=85000,
            stock=12,
            image_url='https://images.unsplash.com/photo-1597733336794-12d05021d510?auto=format&fit=crop&w=800&q=80'
        ),
        Product(
            category=linux_cat,
            name='USB Injection Tool',
            description='Herramienta de automatización HID para auditorías de seguridad.',
            price=45000,
            stock=20,
            image_url='https://images.unsplash.com/photo-1614145121029-83a9f7968944?auto=format&fit=crop&w=800&q=80'
        ),
        Product(
            category=linux_cat,
            name='Teclado Mecánico QMK',
            description='Totalmente programable con firmware Open Source QMK/VIA.',
            price=120000,
            stock=15,
            image_url='https://images.unsplash.com/photo-1518481612222-68bbe828ecd1?auto=format&fit=crop&w=800&q=80'
        ),
        Product(
            category=linux_cat,
            name='RTL-SDR Blog V4',
            description='Radio definida por software compatible con GNU Radio en Linux.',
            price=42000,
            stock=25,
            image_url='https://images.unsplash.com/photo-1631553127988-360660603704?auto=format&fit=crop&w=800&q=80'
        ),
        Product(
            category=linux_cat,
            name='NVMe SSD 1TB - Linux Ready',
            description='Alta velocidad con soporte nativo para sistemas de archivos EXT4 y BTRFS.',
            price=85000,
            stock=30,
            image_url='https://images.unsplash.com/photo-1558494949-ef010cbdcc51?auto=format&fit=crop&w=800&q=80'
        ),
    ])

    # Microsoft products (9 products)
    Product.objects.bulk_create([
        Product(
            category=ms_cat,
            name='Windows 11 Pro - Licencia',
            description='Clave digital original con soporte para BitLocker y Remote Desktop.',
            price=120000,
            stock=100,
            image_url='https://images.unsplash.com/photo-1633419461186-7d40a38105ec?auto=format&fit=crop&w=800&q=80'
        ),
        Product(
            category=ms_cat,
            name='Microsoft Surface Laptop 5',
            description='Pantalla táctil PixelSense y procesador Intel Core i7.',
            price=1250000,
            stock=8,
            image_url='https://images.unsplash.com/photo-1519739010045-233d737c9975?auto=format&fit=crop&w=800&q=80'
        ),
        Product(
            category=ms_cat,
            name='Microsoft 365 Personal',
            description='Suscripción anual: Word, Excel, PowerPoint y 1TB en OneDrive.',
            price=65000,
            stock=50,
            image_url='https://images.unsplash.com/photo-1512428559087-560fa5ceab42?auto=format&fit=crop&w=800&q=80'
        ),
        Product(
            category=ms_cat,
            name='Control Xbox Wireless',
            description='Compatible con Windows 10/11 y conexión Bluetooth.',
            price=55000,
            stock=20,
            image_url='https://images.unsplash.com/photo-1605902711622-cfb43c4437b5?auto=format&fit=crop&w=800&q=80'
        ),
        Product(
            category=ms_cat,
            name='Surface Pro 9',
            description='La versatilidad de una tablet con la potencia de una laptop.',
            price=980000,
            stock=10,
            image_url='https://images.unsplash.com/photo-1541807084-5c52b6b3adef?auto=format&fit=crop&w=800&q=80'
        ),
        Product(
            category=ms_cat,
            name='Dell Precision Workstation',
            description='Optimizada para Windows 11 Pro y diseño CAD profesional.',
            price=2100000,
            stock=4,
            image_url='https://images.unsplash.com/photo-1593642632823-8f785ba67e45?auto=format&fit=crop&w=800&q=80'
        ),
        Product(
            category=ms_cat,
            name='PC Gamer Omen - Win 11',
            description='RTX 4070, 32GB RAM, lista para Xbox Game Pass.',
            price=1450000,
            stock=6,
            image_url='https://images.unsplash.com/photo-1552820728-8b83bb6b773f?auto=format&fit=crop&w=800&q=80'
        ),
        Product(
            category=ms_cat,
            name='Microsoft Ergonomic Mouse',
            description='Diseño premium para productividad extendida en Windows.',
            price=42000,
            stock=15,
            image_url='https://images.unsplash.com/photo-1585565804112-f201f68c48b4?auto=format&fit=crop&w=800&q=80'
        ),
        Product(
            category=ms_cat,
            name='Monitor 4K HDR - Windows Ready',
            description='Soporte nativo para Auto HDR de Windows 11.',
            price=320000,
            stock=12,
            image_url='https://images.unsplash.com/photo-1611078489935-0cb964de46d6?auto=format&fit=crop&w=800&q=80'
        ),
    ])

    # Mac & Apple Silicon products (9 products)
    Product.objects.bulk_create([
        Product(
            category=mac_cat,
            name='MacBook Air M3 - 13"',
            description='Increíblemente delgado y rápido. CPU de 8 núcleos y GPU de hasta 10 núcleos.',
            price=1150000,
            stock=12,
            image_url='https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=800&q=80'
        ),
        Product(
            category=mac_cat,
            name='iPhone 15 Pro Max',
            description='Diseño de titanio, chip A17 Pro y sistema de cámaras avanzado.',
            price=1350000,
            stock=8,
            image_url='https://images.unsplash.com/photo-1510878933023-e2e2e3942fb0?auto=format&fit=crop&w=800&q=80'
        ),
        Product(
            category=mac_cat,
            name='iPad Pro M2 - 11"',
            description='Pantalla Liquid Retina, Apple Pencil Hover y rendimiento brutal.',
            price=890000,
            stock=15,
            image_url='https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?auto=format&fit=crop&w=800&q=80'
        ),
        Product(
            category=mac_cat,
            name='iMac M3',
            description='Todo en uno superdelgado con chip M3 y espectacular pantalla Retina 4.5K.',
            price=1490000,
            stock=5,
            image_url='https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?auto=format&fit=crop&w=800&q=80'
        ),
        Product(
            category=mac_cat,
            name='Mac Mini M2',
            description='Haz más, más rápido. El cerebro de escritorio más asequible y versátil.',
            price=650000,
            stock=10,
            image_url='https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?auto=format&fit=crop&w=800&q=80'
        ),
        Product(
            category=mac_cat,
            name='AirPods Pro 2',
            description='Cancelación de ruido activa mejorada y sonido adaptativo de alta fidelidad.',
            price=240000,
            stock=25,
            image_url='https://images.unsplash.com/photo-1588449668338-d151688c3482?auto=format&fit=crop&w=800&q=80'
        ),
        Product(
            category=mac_cat,
            name='Apple Watch Series 9',
            description='Pantalla más brillante, doble toque interactivo y mediciones de salud avanzadas.',
            price=450000,
            stock=14,
            image_url='https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?auto=format&fit=crop&w=800&q=80'
        ),
        Product(
            category=mac_cat,
            name='Studio Display',
            description='Pantalla Retina 5K de 27 pulgadas con cámara ultra gran angular de 12 MP.',
            price=1690000,
            stock=3,
            image_url='https://images.unsplash.com/photo-1547082299-de196ea013d6?auto=format&fit=crop&w=800&q=80'
        ),
        Product(
            category=mac_cat,
            name='Magic Keyboard con Touch ID',
            description='Teclado inalámbrico y recargable con autenticación Touch ID integrada.',
            price=110000,
            stock=30,
            image_url='https://images.unsplash.com/photo-1587829741301-dc798b83add3?auto=format&fit=crop&w=800&q=80'
        ),
    ])

def reverse_seed(apps, schema_editor):
    Category = apps.get_model('products', 'Category')
    Category.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_data, reverse_code=reverse_seed),
    ]
