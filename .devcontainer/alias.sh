# Add 'test' alias for npx playwright test if it doesn't already exist
if ! grep -q "alias test=" ~/.bashrc; then
    echo "alias test='npx playwright test'" >> ~/.bashrc
fi

# Add 'report' alias for npx playwright show-report --host 0.0.0.0 if it doesn't already exist
if ! grep -q "alias report=" ~/.bashrc; then
    echo "alias report='npx playwright show-report --host 0.0.0.0'" >> ~/.bashrc
fi