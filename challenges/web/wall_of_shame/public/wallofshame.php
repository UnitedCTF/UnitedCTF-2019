<div id="photos">
    <img src="/assets/images/elliot.jpg">
    <img src="/assets/images/neo.jpg">
    <img src="/assets/images/zuck.jpg">
    <img src="/assets/images/hacker.jpg">
    <img src="/assets/images/batman.jpg">
    <img src="/assets/images/mitnick.jpg">
    <img src="/assets/images/sponge.jpeg">
    <img src="/assets/images/trump.jpg">
    <img src="/assets/images/god.jpg">

<?php foreach ($_SESSION["files"] as $file): ?>

    <img src="<?= $_SESSION["folder"] . $file; ?>" />

<?php endforeach; ?>

</div>