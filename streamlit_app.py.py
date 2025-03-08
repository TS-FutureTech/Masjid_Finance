{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3754dc0b-cf92-47e7-ae2f-000c14471c30",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-03-08 13:53:14.322 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\NUtech\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-03-08 13:53:14.327 Session state does not function when running a script without `streamlit run`\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import requests\n",
    "\n",
    "st.title(\"Financial Management App\")\n",
    "\n",
    "st.sidebar.header(\"Navigation\")\n",
    "page = st.sidebar.radio(\"Go to\", [\"Add Record\", \"View Records\", \"Financial Summary\"])\n",
    "\n",
    "if page == \"Add Record\":\n",
    "    st.header(\"Add a New Record\")\n",
    "    record_type = st.selectbox(\"Record Type\", [\"donations\", \"expenditures\", \"assets\"])\n",
    "    name = st.text_input(\"Name/Description\")\n",
    "    amount = st.number_input(\"Amount\", step=0.01)\n",
    "    purpose = st.text_input(\"Purpose (for donations)\")\n",
    "    category = st.text_input(\"Category (for expenditures)\")\n",
    "    condition = st.text_input(\"Condition (for assets)\")\n",
    "    date = st.date_input(\"Date\")\n",
    "    \n",
    "    if st.button(\"Add Record\"):\n",
    "        data = {\n",
    "            'name': name,\n",
    "            'amount': amount,\n",
    "            'purpose': purpose,\n",
    "            'category': category,\n",
    "            'condition': condition,\n",
    "            'date': date.strftime('%Y-%m-%d %H:%M:%S')\n",
    "        }\n",
    "        response = requests.post(f\"http://192.168.100.43:5000/add\", data=data)\n",
    "        if response.status_code == 200:\n",
    "            st.success(\"Record added successfully!\")\n",
    "        else:\n",
    "            st.error(\"Failed to add record.\")\n",
    "\n",
    "elif page == \"View Records\":\n",
    "    st.header(\"View Records\")\n",
    "    table = st.selectbox(\"Select Table\", [\"donations\", \"expenditures\", \"assets\"])\n",
    "    if st.button(\"View\"):\n",
    "        response = requests.get(f\"http://192.168.100.43:5000/view/{table}\")\n",
    "        if response.status_code == 200:\n",
    "            records = response.json()\n",
    "            st.table(records)\n",
    "        else:\n",
    "            st.error(\"Failed to fetch records.\")\n",
    "\n",
    "elif page == \"Financial Summary\":\n",
    "    st.header(\"Financial Summary\")\n",
    "    if st.button(\"Get Summary\"):\n",
    "        response = requests.get(\"http://192.168.100.43:5000/summary\")\n",
    "        if response.status_code == 200:\n",
    "            summary = response.json()\n",
    "            st.write(f\"Total Donations: {summary['total_donations']}\")\n",
    "            st.write(f\"Total Expenditures: {summary['total_expenditures']}\")\n",
    "            st.write(f\"Balance: {summary['balance']}\")\n",
    "            st.write(f\"Total Assets: {summary['total_assets']}\")\n",
    "        else:\n",
    "            st.error(\"Failed to fetch summary.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8d537e78-07f1-4ee5-b410-3253bdb9dea5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
