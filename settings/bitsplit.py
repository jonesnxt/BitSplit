SATOSHI_MOD = pow(10, 8)
BITSPLIT = {
    'database_engine': 'mongo',
    'database_url': 'mongodb://localhost:27017/bitsplit',

    # labels/prefixes
    'xcp_account_prefix': 'BITSPLIT_XCP_',

    # delays and batch sizes
    'btc_batch_size': 20,  # number to run
    'btc_batch_delay': 5 * 60,  # seconds
    'loop_delay': 10,  # seconds

    # costs/fees
    'bitpslit_btc_fee_per_distribution': 0.000078,
    'satoshi_mod': SATOSHI_MOD,
    'xcp_miner_fee': 0.00001,
    'xcp_dust_size': 0.000025,
    #'service_fee': 0,
    'decimals': 8,

    # mailer
    'smtp_host': '',
    'smtp_port': 587,
    'smtp_tls': False,
    'smtp_username': '',
    'smtp_password': '',

    'email_from': '"BitSplit" <noreply@bitsplit.io>',
    'email_to': '',
}

BITSPLIT['xcp_fee_per_to_address'] = \
    (2 * BITSPLIT['xcp_dust_size']) + BITSPLIT['xcp_miner_fee']

from decimal import getcontext

getcontext().prec = BITSPLIT['decimals']
