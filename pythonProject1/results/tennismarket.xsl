<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
    <html xmlns="http://www.w3.org/1999/xhtml">
        <head>
            <title>Goods catalog</title>
        </head>
        <body>
            <h1>Balls catalog</h1>
            <table border = "1">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Price</th>
                        <th>Image</th>
                    </tr>
                </thead >
                <tbody>
                    <xsl:for-each select="items/item">
                        <tr>
                            <td><xsl:value-of select="name"/></td>
                            <td><xsl:value-of select="price"/></td>
                            <td><xsl:value-of select="description"/></td>
                            <td>
                                <xsl:variable name="img_src" select="img"/>
                                <img src="{$img_src}" width="300" />
                            </td>
                        </tr>
                    </xsl:for-each>
                </tbody>
            </table>
        </body>
    </html>
</xsl:template>
</xsl:stylesheet>