<?php
/**
 * User: faisal
 * Date: 15/05/16
 * Time: 20:49
 */

namespace App\Models;

use App\Helpers\DB;


class Computer
{

    static function get($type)
    {
        $sql = "SELECT price, cpu_id, gpu_id, ram, harddisk, monitor FROM computer WHERE type=:type";

        $dbh = DB::connect();
        $computer = $dbh->prepare($sql);

        $computer->execute(
            array(':type' => $type)
        );

        $computer_res = $computer->fetchAll();

        $result = array(
            "computer" => $computer_res,
            "cpu" => CPU::get($computer_res["cpu_id"]),
            "gpu" => GPU::get($computer_res["gpu_id"])
        );

        return $result;
    }

    static function add($type, $price, $cpu_id, $gpu_id, $ram, $harddisk, $monitor)
    {
        $sql = "INSERT INTO computer (type, price, cpu_id, gpu_id, ram, harddsik, monitor) VALUES  (:type, :price, :cpu_id, :gpu_id, :ram, :harddisk, :monitor)";

        $dbh = DB::connect();
        $computer = $dbh->prepare($sql);

        $computer->execute(
            array(
                ':type' => $type,
                ':price' => $price,
                ':cpu_id' => $cpu_id,
                ':gpu_id' => $gpu_id,
                ':ram' => $ram,
                ':harddisk' => $harddisk,
                ':monitor' => $monitor
            )
        );
    }

    static function update($type, $price, $cpu_id, $gpu_id, $ram, $harddisk, $monitor)
    {
        $sql = "UPDATE computer SET price=:price, cpu_id=:cpu_id, gpu_id=:gpu_id, ram=:ram, harddisk=:harddisk, monitor=:monitor WHERE type=:type";
        $dbh = DB::connect();
        $computer = $dbh->prepare($sql);

        $computer->execute(
            array(
                ':type' => $type,
                ':price' => $price,
                ':cpu_id' => $cpu_id,
                ':gpu_id' => $gpu_id,
                ':ram' => $ram,
                ':harddisk' => $harddisk,
                ':monitor' => $monitor
            )
        );
    }

    static function delete($type)
    {
        $sql = "DELETE FROM computer WHERE type=:type";

        $dbh = DB::connect();
        $computer = $dbh->prepare($sql);

        $computer->execute(
            array(':type' => $type)
        );

    }

    static function all()
    {
        $sql = "SELECT price, cpu_id, gpu_id, ram, harddisk, monitor FROM computer";

        $dbh = DB::connect();
        $computer = $dbh->prepare($sql);

        $computer->execute();

        $computer_res = $computer->fetchAll();

        $result = array();

        foreach ($computer_res as $com) {
            array_push($result, array(
                "computer" => $com,
                "cpu" => CPU::get($com["cpu_id"]),
                "gpu" => GPU::get($com["gpu_id"])
            ));
        }

        return $result;
    }
}