(function($) {
    "use strict"; // Start of use strict

    // Method to preload Fav Icon and Password Progress Bar correctly
    $(window).on('load', function() {
        if( $('#formInputFavCheckbox').is(':checked') ) {
            $('.checked').removeClass("d-none");
            $('.unchecked').addClass("d-none");
        } else {
            $('.unchecked').removeClass("d-none");
            $('.checked').addClass("d-none");
        }
        var passwordPercentage = getPasswordPercentage($("#formInputPassword").val());
        changePasswordProgressBar(passwordPercentage);
    });

    // Method to change Fav Icon and checkbox when clicked
    $(".custom-fav-checkbox").on('click', function() {
        if( $('#formInputFavCheckbox').is(':checked') ) {
            $('#formInputFavCheckbox').prop('checked', false);
            $('.unchecked').removeClass("d-none");
            $('.checked').addClass("d-none");
        } else {
            $('#formInputFavCheckbox').prop('checked', true);
            $('.checked').removeClass("d-none");
            $('.unchecked').addClass("d-none");
        }
    });

    $("#formInputPassword").on('input', function() {
        var password = this.value;
        var passwordPercentage = getPasswordPercentage(password);
        changePasswordProgressBar(passwordPercentage);

    });

    function getPasswordPercentage(password) {
        var passwordPercentage = 0;
        if (password) {
            var lowercaseRegExp = new RegExp('(?=.*[a-z])');// 10
            if (lowercaseRegExp.test(password)) {
                passwordPercentage += 10;
            }
            var uppercaseRegExp = new RegExp('(?=.*[A-Z])');// 10
            if (uppercaseRegExp.test(password)) {
                passwordPercentage += 10;
            }
            var numberRegExp = new RegExp('(?=.*[0-9])');// 20
            if (numberRegExp.test(password)) {
                passwordPercentage += 20;
            }
            var SpecialCharRegExp = new RegExp('(?=.*[^A-Za-z0-9])');// 30
            if (SpecialCharRegExp.test(password)) {
                passwordPercentage += 30;
            }
            var lengthRegExp = new RegExp('(?=.{8,})');// 30
            if (lengthRegExp.test(password)) {
                passwordPercentage += 30;
            }
        }
        return passwordPercentage;
    }

    function changePasswordProgressBar(passwordPercentage) {
        $("#password_progress_bar").removeClass();
        if (passwordPercentage == 100) {
            // 100% - Strong
            $("#password_progress_title").text("Strong");
            $("#password_progress_bar").attr("style","width: " + passwordPercentage + "%");
            $("#password_progress_bar").addClass("progress-bar bg-success");
        } else if (passwordPercentage >= 40) {
            // 50% - Medium
            $("#password_progress_title").text("Medium");
            $("#password_progress_bar").attr("style","width: " + passwordPercentage + "%");
            $("#password_progress_bar").addClass("progress-bar bg-warning");
        } else if (passwordPercentage >= 10) {
            // 25% - Weak
            $("#password_progress_title").text("Weak");
            $("#password_progress_bar").attr("style","width: " + passwordPercentage + "%");
            $("#password_progress_bar").addClass("progress-bar bg-danger");
        } else {
            // 0% - Empty
            $("#password_progress_title").text("No password");
            $("#password_progress_bar").attr("style","width: 0%");
        }
    }

})(jQuery); // End of use strict
