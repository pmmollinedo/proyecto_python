(function($) {
    "use strict"; // Start of use strict

    // Method to preload Fav Icon and Password Progress Bar correctly
    $(window).on('load', function() {
        console.log($("#brand_icon_select").val());
    });

    // Trigger to change brand icon (Form + Visual)
    $(".brand-item").on('click', function() {
        // Form login
        var brand_id = $(this).children('.brand-id').val();
        $("#brand_icon_select").val(brand_id);

        // Visual icon logic
        var previousIconClassList = $('#brand_icon_logo').attr('class').split(/\s+/);
        $('#brand_icon_logo').removeClass();
        var newIconClass = $(this).children('.brand-icon-class').val();
        $('#brand_icon_logo').addClass(newIconClass);
        // Set default class items at same position
        $('#brand_icon_logo').addClass(previousIconClassList[2]);
        $('#brand_icon_logo').addClass(previousIconClassList[3]);

        // Close modal
        $('#brandIconsModal').modal('hide');
    });
})(jQuery); // End of use strict
