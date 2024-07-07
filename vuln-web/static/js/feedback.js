
        $(document).ready(function(){
            $('#feedbackForm').submit(function(event){
                event.preventDefault(); // Prevent the form from submitting the traditional way

                var formData = {
        
                    message: $('#message').val()
                };

                $.ajax({
                    type: 'POST',
                    url: '/feedback',
                    async:false,
                    contentType: 'application/json',
                    data: JSON.stringify(formData),
                    success: function(response) {
                        var firstName = encodeURIComponent($('#first_name').val());
                        var lastName = encodeURIComponent($('#last_name').val());
                        window.location.href = '/thank_you?first_name=' + firstName + '&last_name=' + lastName;
                    },
                    error: function(error) {
                        console.log('Error:', error);
                        alert('There was an error processing your request.');
                    }
                });
            });
        });
  