# Copyright(C) 2014 by Abe developers.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/agpl.html>.

from . import BaseChain

import ltc_scrypt

class FakeCoin(BaseChain):
    def __init__(chain, **kwargs):
        chain.name = 'FakeCoin'
        chain.code3 = 'FAK'
        chain.script_addr_vers = "\x7F"
        chain.address_version = "\x7F"
        chain.magic = "\xFB\xC0\xB6\xDB"
        BaseChain.__init__(chain, **kwargs)

    datadir_conf_file_name = "fakecoin.conf"
    datadir_rpcport = 9334
    
    
    def block_header_hash(chain, header):
        b = chain.parse_block_header(header)
        from .. import util
        return util.double_sha256(header)
