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
        <tr>
            <td>faisal</td>
            <td>administrator</td>
            <td>
                <div class="btn-group btn-group-xs" role="group" aria-label="...">
                    <a class="btn btn-danger" href="#" role="button">delete</a>
                    <a class="btn btn-primary" href="#" role="button">edit</a>
                </div>
            </td>
        </tr>
    </tbody>
</table>
<?php $this->stop() ?>