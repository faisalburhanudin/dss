<?php
/**
 * User: faisal
 * Date: 15/05/16
 * Time: 20:48
 */

namespace App\Models;

use App\Helpers\DB;


class GPU
{
    static function get($type)
    {
        $sql = "SELECT memory, speed FROM gpu WHERE type=:type";

        $dbh = DB::connect();
        $gpu = $dbh->prepare($sql);

        $gpu->execute(
            array(':type' => $type)
        );

        return $gpu->fetchAll();
    }

    static function add($type, $memory, $speed)
    {
        $sql = "INSERT INTO gpu (type, memory, speed) VALUES (:type, :memory, :speed)";

        $dbh = DB::connect();
        $gpu = $dbh->prepare($sql);

        $gpu->execute(
            array(
                ':type' => $type,
                ':memory' => $memory,
                ':speed' => $speed
            )
        );
    }

    static function update($type, $memory, $speed)
    {
        $sql = "UPDATE gpu SET type=:type, memory=:memory, speed=:speed WHERE type=:type";

        $dbh = DB::connect();
        $gpu = $dbh->prepare($sql);

        $gpu->execute(
            array(
                ':type' => $type,
                ':memory' => $memory,
                ':speed' => $speed
            )
        );
    }

    static function delete($type)
    {
        $sql = "DELETE FROM gpu WHERE type=:type";

        $dbh = DB::connect();
        $gpu = $dbh->prepare($sql);

        $gpu->execute(
            array(
                ':type' => $type
            )
        );

    }

    static function all()
    {
        $sql = "SELECT memory, speed FROM gpu";

        $dbh = DB::connect();
        $gpu = $dbh->prepare($sql);
        $gpu->execute();

        return $gpu->fetchAll();
    }
}