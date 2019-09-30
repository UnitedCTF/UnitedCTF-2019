<?php

if (isset($_POST["flag"]))
{
    $is_valid = false;
    $flag = file_get_contents("/flag.txt");
    if ($_POST["flag"] === $flag) {
        $is_valid = true;
    }
}
?>

<p>What is the flag? Show me your skillz.</p>
<form method="post">
    <div class="form-group">
        <input type="text" name="flag" class="form-control" aria-describedby="flagHelp" placeholder="Enter flag">
    </div>
    <button type="submit" class="btn btn-primary">Submit</button>
</form>

<?php if (isset($_POST["flag"]) || isset($_FILES["picture"])): ?>

    <hr>

    <?php if ($is_valid): ?>

        <p class="success">Correct!</p>
        <p>You are a master hacker, good job!</p>

    <?php else: ?>

        <?php if (isset($_FILES["picture"])): ?>

            <div class="alert alert-danger" role="alert">
                <?= $error; ?>
            </div>

        <?php endif; ?>

        <p class="fail">Wrong.</p>
        <p>You are obviously not a real hacker, you should add your picture to the Wall of Shame.</p>

        <form method="post" enctype="multipart/form-data">
            <div class="form-group">
                <input type="file" name="picture" class="form-control-file">
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>

    <?php endif; ?>

<?php endif; ?>
