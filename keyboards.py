# Updated script with fixes applied to show_cart and handle_quantity handlers.
file_path = 'a.py'

# Reading the content of the file.
with open(file_path, 'r') as file:
    lines = file.readlines()

# Updating the relevant handlers
for i, line in enumerate(lines):
    if "async def show_cart(message: types.Message, state: FSMContext):" in line:
        # Updating the show_cart handler
        lines[i:i+10] = [
            "async def show_cart(message: types.Message, state: FSMContext):\n",
            "    user_id = message.from_user.id\n",
            "    user_data = await state.get_data()\n",
            "    if 'cart' in user_data.get(user_id, {}):\n",
            "        cart_items = user_data[user_id]['cart']\n",
            "        response = \"Your cart contains:\\n\" + \"\\n\".join(f\"{item['name']}: {item['quantity']}\" for item in cart_items)\n",
            "    else:\n",
            "        response = \"Your cart is empty.\"\n",
            "    await message.answer(response)\n",
        ]
    if "async def handle_quantity(message: types.Message, state: FSMContext):" in line:
        # Updating the handle_quantity handler
        lines[i:i+12] = [
            "async def handle_quantity(message: types.Message, state: FSMContext):\n",
            "    user_id = message.from_user.id\n",
            "    quantity = message.text\n",
            "    async with state.proxy() as user_data:\n",
            "        if user_id not in user_data:\n",
            "            user_data[user_id] = {}\n",
            "        if 'cart' not in user_data[user_id]:\n",
            "            user_data[user_id]['cart'] = []\n",
            "        # Add item to cart with quantity (assuming item name is predefined, modify as needed)\n",
            "        user_data[user_id]['cart'].append({\"name\": \"Item\", \"quantity\": quantity})\n",
            "    await state.reset_state(with_data=False)\n",
            "    await message.answer(f\"Added {quantity} of Item to your cart.\")\n",
        ]

# Writing the corrected content back to the file.
with open(file_path, 'w') as file:
    file.writelines(lines)
