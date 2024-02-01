import streamlit as st 


# Display an image with a caption that provides context for the BMI calculator
st.image('adult-body-mass-index-guide-alt-1440x810.jpg', caption='Source: https://www.everydayhealth.com/')

# Application title
st.title('Body Mass Index (BMI)')

# Description header explaining the purpose of the BMI calculation
st.header('Do you have a healthy body weight?')
st.caption('ps.: do not trust this application completely. The BMI has several limitation. Check your health with a proper specialist.')

# User input for weight in kilograms
weight = st.number_input('Insert the weight (in kgs)', value=0.0)
st.write('The weight is ', weight, ' kgs')

# User input for height in meters
height = st.number_input('Insert the height (in meters)', value=0.0)
st.write('The height is ', height, ' meters')

# Calculate BMI if height is not zero to avoid division by zero error
if(height != 0):
    imc = weight/(height ** 2)
else:
    imc= 0

# Function to categorize BMI result
def checkIMC(imc):
    if(imc < 18.5):
        return 'Underweight'
    elif((imc >= 18.5) & (imc < 24.99)):
        return 'Normal weight'
    elif((imc >= 25) & (imc < 29.99 ) ):
        return 'Overweight'
    elif(imc >= 30 ):
        return 'Obesity'
    else:
        return 'Check input'

# Determine the BMI category
type = checkIMC(imc)

# Divider for layout
st.divider()

# Display the user's BMI result and category
st.header('YOUR RESULT:')
st.subheader(f'Your BMI is {imc:.2f} this means you have: {type}')

# Divider for layout
st.divider()

# Markdown sections for BMI categories and limitations for better user information
st.markdown("## BMI Categories")
st.markdown("- **Underweight:** BMI less than 18.5")
st.markdown("- **Normal weight:** BMI between 18.5 and 24.9")
st.markdown("- **Overweight:** BMI between 25 and 29.9")
st.markdown("- **Obesity:** BMI 30 or above")
st.markdown("## Limitations of BMI")
st.markdown("While BMI is a useful general guideline, it does not directly measure body fat or account for muscle mass, bone density, overall body composition, and racial and sex differences. Therefore, it should be considered alongside other measurements and assessments for a more accurate picture of an individual's health status.")
