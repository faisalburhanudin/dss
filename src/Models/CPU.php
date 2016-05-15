<?php
/**
 * User: faisal
 * Date: 15/05/16
 * Time: 20:45
 */

namespace App\Models;

use App\Helpers\DB;

class CPU
{

    static function get($type)
    {
        $sql = "SELECT core, speed, cache FROM cpu WHERE type=:type";

        $dbh = DB::connect();
        $cpu = $dbh->prepare($sql);

        $cpu->execute(
            array(':id' => $type)
        );

        return $cpu->fetchAll();
    }

    static function add($type, $core, $speed, $cache)
    {
        $sql = "INSERT INTO cpu (type, core, speed, cache) VALUES (:type, :core, :speed, :cache)";

        $dbh = DB::connect();
        $cpu = $dbh->prepare($sql);

        $cpu->execute(array(
            ":type" => $type,
            ":core" => $core,
            ":speed" => $speed,
            ":cache" => $cache
        ));
    }

    static function update($type, $core, $speed, $cache)
    {
        $sql = "UPDATE cpu SET core=:core, speed=:speed, cache=:cache WHERE type=:type";

        $dbh = DB::connect();
        $cpu = $dbh->prepare($sql);

        $cpu->execute(array(
            ":type" => $type,
            ":core" => $core,
            ":speed" => $speed,
            ":cache" => $cache
        ));
    }

    static function delete($type)
    {
        $sql = "DELETE FROM cpu WHERE type=:type";

        $dbh = DB::connect();
        $cpu = $dbh->prepare($sql);

        $cpu->execute(array(
            ":type" => $type
        ));
    }

    static function all()
    {
        $sql = "SELECT core, speed, cache FROM cpu";

        $dbh = DB::connect();
        $cpu = $dbh->prepare($sql);
        $cpu->execute();

        return $cpu->fetchAll();
    }

}