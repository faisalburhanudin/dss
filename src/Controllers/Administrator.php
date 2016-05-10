<?php
/**
 * User: faisal
 * Date: 5/7/16
 * Time: 7:57 PM
 */

namespace App\Controllers;
use App\Helpers\DB;


class Administrator {

     /**
     * Get list users administrator
     */
    static function listAdministrators(){
        $dbh = DB::connect();

        $user = $dbh->query("SELECT id, username, password, status FROM administrator");

        return $user->fetchAll();
    }
}