from .utils import pluralise

ALL = 'ALL'
GET = 'GET'
POST = 'POST'
PUT = 'PUT'
DELETE = 'DELETE'
CRUD = 'CRUD'  # shorthand for creating the ALL|GET|POST|PUT|DELETE endpoints in one swoop

METHOD_ORDER = [ALL, GET, POST, PUT, DELETE]

ENDPOINTS = {
    'Banking/': {
        'name': 'banking',
        'methods': [
            (ALL, '', 'banking type'),
            (CRUD, 'SpendMoneyTxn/', 'spend money transaction'),
            (CRUD, 'ReceiveMoneyTxn/', 'receive money transaction'),
        ],
    },
    'Contact/': {
        'name': 'contacts',
        'methods': [
            (ALL, '', 'contact type'),
            (CRUD, 'Customer/', 'customer contact'),
            (CRUD, 'Supplier/', 'supplier contact'),
        ],
    },
    'Sale/Invoice/': {
        'name': 'invoices',
        'methods': [
            (ALL, '', 'sale invoice type'),
            (CRUD, 'Item/', 'item type sale invoice'),
            (CRUD, 'Service/', 'service type sale invoice'),
        ]
    },
    'GeneralLedger/': {
        'name': 'general_ledger',
        'methods': [
            (CRUD, 'TaxCode/', 'tax code'),
            (CRUD, 'Account/', 'account'),
            (CRUD, 'Category/', 'cost center tracking category'),
        ]
    },
    'Inventory/': {
        'name': 'inventory',
        'methods': [
            (CRUD, 'Item/', 'inventory item'),
        ]
    },
    'Purchase/Order/': {
        'name': 'purchase_orders',
        'methods': [
            (ALL, '', 'purchase order type'),
            (CRUD, 'Item/', 'item type purchase order'),
        ]
    },
    'Purchase/Bill/': {
        'name': 'purchase_bills',
        'methods': [
            (ALL, '', 'purchase bill type'),
            (CRUD, 'Item/', 'item type purchase bill'),
            (CRUD, 'Service/', 'service type purchase bill'),
            (CRUD, 'Miscellaneous/', 'miscellaneous type purchase bill'),
        ]
    },
}

METHOD_MAPPING = {
    ALL: {
        'endpoint': lambda base: base,
        'hint': lambda name: 'Return all %s for an AccountRight company file.' % pluralise(name)
    },
    GET: {
        'endpoint': lambda base: base + '[uid]/',
        'hint': lambda name: 'Return selected %s.' % name
    },
    PUT: {
        'endpoint': lambda base: base + '[uid]/',
        'hint': lambda name: 'Update selected %s.' % name
    },
    POST: {
        'endpoint': lambda base: base,
        'hint': lambda name: 'Create new %s.' % name
    },
    DELETE: {
        'endpoint': lambda base: base + '[uid]/',
        'hint': lambda name: 'Delete selected %s.' % name
    },
}
