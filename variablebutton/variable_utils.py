class VariableDeliveryHandler(IPythonHandler):
    def get(self):
        try:
            order = build_order()
            items=_parse_items()
            place_order(order,items)
            msg_json = build_msg_json(
                title="Yay it works :-D",
                body="Your order of {}\nis on the way".format(items)
            )
        except MissingVariableVarError as e:
            msg_json=build_msg_json(title="Variables Missing",body=e.err_msg)
            self.write(msg_json)
            self.flush()
            