<?php
/**
 * User: faisal
 * Date: 5/7/16
 * Time: 8:01 PM
 */

namespace Spk\Helpers;
use PDO;


class DB {

    /**
     * Create connection
     *
     * @return PDO object
     */
    public static function connect()
    {
        $dbhost = getenv("dbhost");
        $dbuser = getenv("dbuser");
        $dbpass = getenv("dbpass");
        $dbname = getenv("dbname");

        $dsn = sprintf('mysql:host=%s;dbname=%s', $dbhost, $dbname);
        $options = array(
            PDO::MYSQL_ATTR_INIT_COMMAND => 'SET NAMES utf8',
        );

        $dbh = new PDO($dsn, $dbuser, $dbpass, $options);

        return $dbh;
    }
}