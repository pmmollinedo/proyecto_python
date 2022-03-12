(function($) {
    "use strict"; // Start of use strict

    // Trigger to change brand icon (Form + Visual)
    $(".avatar-item").on('click', function() {
        // Form login
        var avatar_name = $(this).children('.avatar-item-name').val();
        $("#formInputProfileAvatar").val(avatar_name);

        // Visual icon logic
        var avatar_img_source = $(this).children('.card-image').attr("src");
        $("#profile_avatar_img").attr("src",avatar_img_source);

        // Close modal
        $('#profileAvatarModal').modal('hide');
    });
})(jQuery); // End of use strict
