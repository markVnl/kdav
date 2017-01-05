<?php
/***********************************************
* File      :   KopanoDavBackendTest.php
* Project   :   KopanoDAV
* Descr     :   Tests for Kopano DAV backend class which
*               handles Kopano related activities.
*
* Created   :   27.12.2016
*
* Copyright 2016 Kopano b.v.
*
* This program is free software: you can redistribute it and/or modify
* it under the terms of the GNU Affero General Public License, version 3,
* as published by the Free Software Foundation.
*
* This software uses SabreDAV, an open source software distributed
* under three-clause BSD-license. Please see <http://sabre.io/dav/>
* for more information about SabreDAV.
*
* This program is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
* GNU Affero General Public License for more details.
*
* You should have received a copy of the GNU Affero General Public License
* along with this program.  If not, see <http://www.gnu.org/licenses/>.
*
* Consult LICENSE file for details
************************************************/

namespace Kopano\DAV;

class KopanoDavBackendTest extends \PHPUnit_Framework_TestCase {
    protected $kDavBackend;

    public function setUp() {
        $this->kDavBackend = new KopanoDavBackend(null);
    }

    public function tearDown() {
        $this->kDavBackend = null;
    }

    /**
     * Tests if the constructor is created without errors.
     *
     * @access public
     * @return void
     */
    public function testConstruct() {
        $this->assertTrue(is_object($this->kDavBackend));
    }

}