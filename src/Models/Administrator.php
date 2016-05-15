<?php
/**
 * User: faisal
 * Date: 15/05/16
 * Time: 20:50
 */

namespace App\Models;

use App\Helpers\DB;


class Administrator
{

    static function get($id)
    {

        $sql = "SELECT username status FROM administrator WHERE id=:id";

        $dbh = DB::connect();
        $user = $dbh->prepare($sql);

        $user->execute(
            array(':id' => $id)
        );

        return $user->fetchAll();
    }

    static function add($username, $password)
    {
        $sql = "INSERT INTO administrator (username, password) VALUES (:username, :password)";

        $dbh = DB::connect();
        $user = $dbh->prepare($sql);

        // todo hash password
        $user->execute(
            array(
                ':username' => $username,
                ':password' => $password
            )
        );
    }

    static function update($id, $username, $password)
    {
        $sql = "UPDATE administrator SET username=:username, password=:password WHERE id=:id";

        $dbh = DB::connect();
        $user = $dbh->prepare($sql);

        $user->execute(
            array(
                ':id' => $id,
                ':username' => $username,
                ':password' => $password
            )
        );
    }

    static function delete($id)
    {
        $sql = "DELETE FROM administrator WHERE id=:id";

        $dbh = DB::connect();
        $user = $dbh->prepare($sql);


        $user->execute(
            array(
                ':id' => $id
            )
        );
    }

    static function all()
    {
        $sql = "SELECT username status FROM administrator";

        $dbh = DB::connect();
        $user = $dbh->prepare($sql);

        $user->execute();

        return $user->fetchAll();
    }
}