<?php $this->layout('admin/layout') ?>

<?php $this->start('page') ?>
<a class="btn btn-primary" href="#" role="button">Tambah user</a>
<h2></h2>
<table class="table table-hover">
    <thead>
        <tr>
            <th>Username</th>
            <th>Status</th>
            <th>action</th>
        </tr>
    </thead>
    <tbody>
        <?php foreach($administrator as $row ){ ?>
        <tr>
            <td><?= $row["username"] ?></td>
            <td><?= $row["status"] ?></td>
<!--            todo link edit delete-->
            <td>
                <div class="btn-group btn-group-xs" role="group" aria-label="...">
                    <a class="btn btn-danger" href="#" role="button">delete</a>
                    <a class="btn btn-primary" href="#" role="button">edit</a>
                </div>
            </td>
        </tr>
        <?php }?>
    </tbody>
</table>
<?php $this->stop() ?>